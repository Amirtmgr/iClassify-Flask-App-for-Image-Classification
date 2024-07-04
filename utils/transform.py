from PIL import Image
from torchvision import transforms as T
import json


# Load ImageNet class index
imagenet_index = json.load(open("utils/imagenet_class_index.json"))


# Define the image processing pipeline for IMAGENET datasets
def transform_image(image_bytes):
    my_transforms = T.Compose([
        T.Resize(224),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_bytes)
    return my_transforms(image).unsqueeze(0)
