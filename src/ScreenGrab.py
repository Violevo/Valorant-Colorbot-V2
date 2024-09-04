from requirements import *
from settings import *


import dxcam
from PIL import Image

# Create camera instance
camera = dxcam.create()

# Capture a frame
frame = camera.grab()

# Convert frame to an Image object
image = Image.fromarray(frame)

# Save the image to a file
image.save("image.png", "PNG")
