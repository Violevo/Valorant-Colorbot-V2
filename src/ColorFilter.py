import cv2
import numpy as np
 
 
def get_similarity_map(image_hsv, target_hsv, hue_threshold, similarity_threshold):
    delta = np.abs(image_hsv - target_hsv)
    delta[:, :, 0] = np.minimum(delta[:, :, 0], 180 - delta[:, :, 0]) / 180
    delta[:, :, 1] /= 255
    delta[:, :, 2] /= 255
 
    similarity = 1 - np.sqrt(np.sum(delta[:, :, :] ** 2, axis=2)) / np.sqrt(3)
    mask = np.logical_and(
        delta[:, :, 0] <= hue_threshold,
        np.logical_and(
            similarity_threshold[0] <= similarity, similarity <= similarity_threshold[1]
        ),
    )
 
    return np.where(mask, similarity, 0)
 
 
purple = (150, 119, 179)
hue_threshold = 0.005
similarity_threshold = (0.75, 0.85)
crop_size = 1080
 
 
frame = cv2.imread("image.png")
 
height, width = frame.shape[:2]
roi_x = width // 2 - crop_size // 2
roi_y = height // 2 - crop_size // 2
roi = frame[roi_y : roi_y + crop_size, roi_x : roi_x + crop_size]
 
roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
cv2.imwrite("new.png", roi)
roi = np.array(roi, dtype=np.float32)
 
similarity_map = get_similarity_map(roi, purple, hue_threshold, similarity_threshold)
 
# Show image(for debug)
similarity_map = (similarity_map * 255).astype(np.uint8)
cv2.imshow("img", similarity_map)
cv2.imwrite("new.png", similarity_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
