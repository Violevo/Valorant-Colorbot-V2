from requirements import *
from settings import *
from ScreenGrab import *
from ColorFilter import *

# Load the similarity map
image = Image.open('new.png')

# Convert the image to a numpy array
image_array = np.array(image)

# Find the indices of all white pixels
white_pixels = np.argwhere(image_array != 0)

# Find the topmost white pixel and centre
topmost_white_pixel = white_pixels[white_pixels[:, 0].argmin()] # y, x
center = int(crop_size / 2), int(crop_size / 2)

#subtract the two to create a vector
vector = center - topmost_white_pixel

print(vector)
