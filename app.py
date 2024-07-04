import os
import io
import sys
import json

from flask import Flask, request, jsonify
from models.model import infer_topk
from utils.utils import allowed_file

# Path for Dockerized app
sys.path.append('/app')
FILE_TYPES = set(['png', 'jpg', 'jpeg'])


# Flask
app = Flask(__name__)
app.debug = os.environ.get('DEBUG', False)



# Home Page
@app.route('/', methods=['GET', 'POST'])
def index():
    with open('static/index.html') as f:
        home_page = f.read()
    return home_page


@app.route('/predict', methods=['POST'])
def predict():
    r = {'result': 'No attached file'}

    # Post request
    if request.method == 'POST' and 'image' in request.files:
        
        try:
            topk = int(request.args.get('topk', 5))
            image_bytes = request.files['image']
            
            if image_bytes and allowed_file(image_bytes.filename):
                # Inference
                topk_results = infer_topk(image_bytes, topk)
                return jsonify(topk_results)

        except Exception as e:
            r['result'] = f"Exception {type(e)}: {str(e)}"
    
    return jsonify(r)

    

if __name__ == "__main__":
    app.run()