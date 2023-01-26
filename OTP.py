import os
from PIL import Image

# Open the original image
original_image = Image.open("org.jpg")

# Open the key image
key_image = Image.open("key.jpg")

# Get the pixel data for both images
original_pixels = original_image.load()
key_pixels = key_image.load()

# Get the width and height of the images
width, height = original_image.size

# Create a new image to store the encrypted version
encrypted_image = Image.new("RGB", (width, height))
encrypted_pixels = encrypted_image.load()

# Iterate through the pixels of the original image
for y in range(height):
    for x in range(width):
        # Get the pixel value for the original image
        original_pixel = original_pixels[x, y]
        # Get the pixel value for the key image
        key_pixel = key_pixels[x, y]
        # Use bitwise XOR to encrypt the pixel value
        encrypted_pixel = tuple(a^b for a, b in zip(original_pixel, key_pixel))
        # Set the pixel value in the encrypted image
        encrypted_pixels[x, y] = encrypted_pixel

# Save the encrypted image
encrypted_image.save("encrypted.jpg")