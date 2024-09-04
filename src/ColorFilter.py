from requirements import *
from settings import *

def get_similarity_map(image_hsv, lower_bound_hsv, upper_bound_hsv, hue_threshold, similarity_threshold):    
    delta_lower = np.abs(image_hsv - lower_bound_hsv)
    delta_upper = np.abs(image_hsv - upper_bound_hsv)
    
    # Handle hue wrapping
    delta_lower[:, :, 0] = np.minimum(delta_lower[:, :, 0], 180 - delta_lower[:, :, 0]) / 180
    delta_upper[:, :, 0] = np.minimum(delta_upper[:, :, 0], 180 - delta_upper[:, :, 0]) / 180
    
    delta_lower[:, :, 1] /= 255
    delta_lower[:, :, 2] /= 255
    
    delta_upper[:, :, 1] /= 255
    delta_upper[:, :, 2] /= 255
    
    similarity_lower = 1 - np.sqrt(np.sum(delta_lower ** 2, axis=2)) / np.sqrt(3)
    similarity_upper = 1 - np.sqrt(np.sum(delta_upper ** 2, axis=2)) / np.sqrt(3)
    
    mask = np.logical_and(
        delta_lower[:, :, 0] <= hue_threshold,
        delta_upper[:, :, 0] <= hue_threshold
    )
    mask = np.logical_and(
        mask,
        np.logical_and(
            similarity_threshold[0] <= similarity_lower,
            similarity_upper <= similarity_threshold[1]
        )
    )
    
    return np.where(mask, similarity_lower, 0)

# Load the image
frame = cv2.imread("image.png")
if frame is None:
    raise FileNotFoundError("The image file was not found or could not be loaded.")

height, width = frame.shape[:2]

# Ensure crop size is within image bounds
crop_size = min(crop_size, height, width)

roi_x = width // 2 - crop_size // 2
roi_y = height // 2 - crop_size // 2
roi = frame[roi_y:roi_y + crop_size, roi_x:roi_x + crop_size]


# Convert ROI to HSV color space
roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi = np.array(roi, dtype=np.float32)

# Compute similarity map
similarity_map = get_similarity_map(roi, purple_hsv_lower, purple_hsv_upper, hue_threshold, similarity_threshold)

# Show image (for debug)
similarity_map = (similarity_map * 255).astype(np.uint8)
cv2.imshow("Similarity Map", similarity_map)
cv2.imwrite("new.png", similarity_map)
cv2.waitKey(0)
cv2.destroyAllWindows()

