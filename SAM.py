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


def draw_mask_numbers(image, masks):
    output = image.copy()

    for mask in masks:
        x = mask['x']
        y = mask['y']
        number = mask['number']

        cv2.putText(output, str(number), (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    return output



for i,mask in enumerate(masks):
    mask['number']= i+1

labeled_image = draw_mask_numbers(image, masks)

# cv2.imwrite("labeled_image.png", labeled_image)

print (masks)


# plt.figure(figsize=(20,20))
# plt.imshow(image)
# show_anns(masks)
# plt.axis('off')
# plt.show()






# def auto_segment_abdomen(image_path):
#     image = cv2.imread(image_path)
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



#     overlay = image_rgb.copy()
#     muscle_list = []

#     for i, mask_data in enumerate(masks[:len(abdomen_muscles)]):  # Limit to known muscles
#         muscle_id = i + 1
#         muscle_info = abdomen_muscles.get(muscle_id, None)
#         if muscle_info is None:
#             continue

#         mask = mask_data["segmentation"]
#         color = muscle_info["color"]

#         contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         cv2.drawContours(overlay, contours, -1, color, thickness=2)

#         # Find center of mask
#         M = cv2.moments(mask.astype(np.uint8))
#         if M["m00"] != 0:
#             cx = int(M["m10"] / M["m00"])
#             cy = int(M["m01"] / M["m00"])
#         else:
#             cx, cy = 50 + i * 50, 50  # Fallback

#         # Overlay number
#         cv2.putText(overlay, str(muscle_id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

#         # Add to list
#         muscle_list.append(f"{muscle_id}. {muscle_info['name']}")

#     # Save and show
#     output_path = "abdomen_auto_segmented.jpg"
#     cv2.imwrite(output_path, cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR))
#     print("Segmented image saved as:", output_path)

#     print("\n🧠 Muscle Labels:")
#     for label in muscle_list:
#         print(label)