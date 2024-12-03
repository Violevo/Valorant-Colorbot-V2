# Import user settings
from settings import *  

import subprocess
import sys

def install_package(package_name, import_name=None):
    import_name = import_name or package_name
    try:
        __import__(import_name)
    except ImportError:
        print(f"Package: [{package_name}] not found, installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"Package: [{package_name}] installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install package: [{package_name}]. Error: {e}")

# Handle packages
install_package("opencv-python-headless", "cv2")
install_package("numpy")
install_package("pillow", "PIL")
install_package("dxcam")

import cv2
import numpy
from PIL import Image
import dxcam

def Screen_Grab():
    camera = dxcam.create()
    frame = camera.grab()
    if frame is None:
        raise RuntimeError("Failed to grab frame from the screen.")
    image = Image.fromarray(frame)
    image.save("image.png", "PNG")

def Color_Filter():
    def get_similarity_map(image_hsv):
        delta_lower = numpy.abs(image_hsv - purple_hsv_lower)
        delta_upper = numpy.abs(image_hsv - purple_hsv_upper)
        
        delta_lower[:, :, 0] = numpy.minimum(delta_lower[:, :, 0], 180 - delta_lower[:, :, 0]) / 180
        delta_upper[:, :, 0] = numpy.minimum(delta_upper[:, :, 0], 180 - delta_upper[:, :, 0]) / 180

        delta_lower[:, :, 1:] /= 255
        delta_upper[:, :, 1:] /= 255
        
        similarity_lower = 1 - numpy.sqrt(numpy.sum(delta_lower ** 2, axis=2)) / numpy.sqrt(3)
        similarity_upper = 1 - numpy.sqrt(numpy.sum(delta_upper ** 2, axis=2)) / numpy.sqrt(3)

        mask = numpy.logical_and(
            delta_lower[:, :, 0] <= hue_threshold,
            delta_upper[:, :, 0] <= hue_threshold
        )
        mask = numpy.logical_and(
            mask,
            numpy.logical_and(
                similarity_threshold[0] <= similarity_lower,
                similarity_upper <= similarity_threshold[1]
            )
        )
        
        return numpy.where(mask, similarity_lower, 0)

    frame = cv2.imread("image.png")
    if frame is None:
        raise FileNotFoundError("The image file was not found.")
    
    height, width = frame.shape[:2]
    crop = min(crop_size, height, width)
    roi_x, roi_y = width // 2 - crop // 2, height // 2 - crop // 2
    roi = frame[roi_y:roi_y + crop, roi_x:roi_x + crop]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV).astype(numpy.float32)

    similarity_map = get_similarity_map(roi)
    processed_map = (similarity_map * 255).astype(numpy.uint8)
    cv2.imshow("Similarity Map", processed_map)
    cv2.imwrite("new.png", processed_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    Screen_Grab()
    Color_Filter()

    image = Image.open('new.png')
    image_array = numpy.array(image)
    white_pixels = numpy.argwhere(image_array != 0)
    if white_pixels.size > 0:
        topmost_white_pixel = white_pixels[white_pixels[:, 0].argmin()]
        center = (crop_size // 2, crop_size // 2)
        vector = numpy.array(center) - topmost_white_pixel
        print(f"Vector to topmost white pixel: {vector}")
    else:
        print("No white pixels found.")

if __name__ == "__main__":
    main()
