import torch
from torchvision.models import resnet50, ResNet50_Weights, vit_b_32, ViT_B_32_Weights, efficientnet_v2_l, EfficientNet_V2_L_Weights

from utils.transform import transform_image, imagenet_index


# Load Pretrained Model
model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model.eval()

# Load EfficientNet Model
#model = efficientnet_v2_l(weights=EfficientNet_V2_L_Weights.IMAGENET1K_V1)
#model.eval()

# Load ViT Model
#model = vit_b_32(weights=ViT_B_32_Weights.IMAGENET1K_V1)
#model.eval()


# Inference for top 5 predictions
def infer_topk(image_bytes: bytes, k=1) -> dict[dict]:
    tensor = transform_image(image_bytes)

    with torch.no_grad():
        model_output = model.forward(tensor)
        print(model_output)
        _, indices = torch.sort(model_output, descending=True)
        percentages = torch.nn.functional.softmax(model_output, dim=1)[0]
        top_k = {}
        for i in range(k):
            idx = indices[0][i].item()
            class_id, class_name = imagenet_index[str(idx)]
            confidence = percentages[idx].item()
            top_k[i+1] = {'class_id': class_id,
                        'class name': class_name,
                        'confidence %': f'{confidence:.3%}'}
        print(top_k)
        return top_k
