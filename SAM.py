import torch
import torchvision
import numpy as np
from numpy import shape
import torch
import matplotlib.pyplot as plt
import cv2
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor



def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    ax.imshow(img)


image = cv2.imread('abdominals.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20,20))
plt.imshow(image)
plt.axis('off')
plt.show()

import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor

sam_checkpoint = "sam_vit_h_4b8939.pth"
model_type = "vit_h"



sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)


mask_generator = SamAutomaticMaskGenerator(sam)

masks = mask_generator.generate(image)











plt.figure(figsize=(20,20))
plt.imshow(image)
show_anns(masks)

for i, mask_data in enumerate(masks):
    x, y, w, h = mask_data['bbox']
    center_x = x + w / 2
    center_y = y + h / 2
    plt.text(center_x, center_y, str(i + 1),
             fontsize=12, color='white', ha='center', va='center',
             bbox=dict(facecolor='black', alpha=0.5, boxstyle='round'))


plt.axis('off')
plt.show()






