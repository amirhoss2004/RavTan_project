


import numpy as np
import cv2
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator
import sys
import io

# Helper function to draw annotations, no changes needed here.
def show_anns(anns):
    if not anns:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    
    # Create a transparent overlay for the masks
    h, w = sorted_anns[0]['segmentation'].shape
    overlay = np.ones((h, w, 4))
    overlay[:, :, 3] = 0
    
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]]) # Color with some transparency
        overlay[m] = color_mask
        
    ax.imshow(overlay)

def process_and_segment_image(image_bytes, chat_id, status_callback):
    """
    This single function now handles the entire workflow.
    It takes the image bytes from the Telegram message, processes it,
    and returns the final segmented image as bytes.
    """
    try:
        # --- 1. Decode the Image and Check for Errors ---
        status_callback(chat_id, "Decoding image... 🖼️")
        nparr = np.frombuffer(image_bytes, np.uint8)
        image_bgr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # !! CRITICAL FIX: Check if the image was loaded correctly !!
        if image_bgr is None:
            status_callback(chat_id, "❌ Error: Could not read the image. It might be in an unsupported format. Please try another one.")
            return None

        status_callback(chat_id, "Image quality check passed ✅. Converting color space...")
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

        # --- 2. Load the SAM Model and Generator ---
        # Note: For better performance, you could load the model once when the bot starts.
        status_callback(chat_id, "Loading segmentation model...")
        sys.path.append("..") # Ensure this path is correct for your project structure
        sam_checkpoint = "sam_vit_h_4b8939.pth" # Ensure this file is downloaded and accessible
        model_type = "vit_h"
        
        sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
        mask_generator = SamAutomaticMaskGenerator(sam)

        # --- 3. Generate the Segmentation Masks ---
        status_callback(chat_id, "SAM is segmenting the picture for you... ⏳")
        masks = mask_generator.generate(image_rgb)
        status_callback(chat_id, "SAM's work is done! Labeling segments... 🔢")

        # --- 4. Create the Final Annotated Image ---
        plt.figure(figsize=(12, 12)) # Adjusted size for better performance
        plt.imshow(image_rgb)
        show_anns(masks) # Overlay the colored masks

        # Add number labels to the center of each mask's bounding box
        for i, mask_data in enumerate(masks):
            x, y, w, h = mask_data['bbox']
            center_x, center_y = x + w / 2, y + h / 2
            plt.text(center_x, center_y, str(i + 1),
                     fontsize=12, color='white', weight='bold', ha='center', va='center',
                     bbox=dict(facecolor='black', alpha=0.5, boxstyle='round'))
        
        plt.axis('off')
        
        # --- 5. Save the Image to Memory instead of a File ---
        # This is more efficient and avoids file conflicts.
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
        buf.seek(0) # Rewind the buffer to the beginning
        plt.close() # Free up memory used by the plot

        status_callback(chat_id, "Image is ready to go! 🎉")
        
        # Return the image bytes, ready to be sent
        return buf

    except Exception as e:
        print(f"An error occurred in process_and_segment_image: {e}")
        status_callback(chat_id, f"An unexpected error occurred: {e}")
        return None

