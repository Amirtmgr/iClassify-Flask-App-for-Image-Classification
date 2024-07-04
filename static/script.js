document.getElementById('image-input').addEventListener('change', function(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const img = document.getElementById('selected-image');
        img.src = reader.result;
        img.style.display = 'block';
        document.getElementById('image-container').style.display = 'block';
        document.getElementById('clear-btn').style.display = 'inline-block';
    }
    reader.readAsDataURL(event.target.files[0]);
});

document.getElementById('clear-btn').addEventListener('click', function() {
    const imgInput = document.getElementById('image-input');
    imgInput.value = '';
    document.getElementById('image-container').style.display = 'none';
    document.getElementById('selected-image').src = '#';
    document.getElementById('result').style.display = 'none';
    document.getElementById('result').innerHTML = '';
    this.style.display = 'none';
});

document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const loading = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
    loading.style.display = 'block';
    resultDiv.style.display = 'none';
    
    fetch('/predict?topk=5', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loading.style.display = 'none';
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = '';
        
        Object.keys(data).forEach(key => {
            const item = data[key];
            const resultItem = document.createElement('div');
            resultItem.classList.add('result-item');
            resultItem.innerHTML = `<strong>${item['class name']}</strong> (${item['class_id']}): ${item['confidence %']}`;
            resultDiv.appendChild(resultItem);
        });
    })
    .catch(error => {
        loading.style.display = 'none';
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = 'Error processing the image.';
    });
});
