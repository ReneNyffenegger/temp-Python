import noise
from PIL import Image
import random

# Set the size of the grid
width, height = 400, 320

# Create a new RGB image with the specified size
img = Image.new('RGB', (width, height))

# Generate Perlin noise for each pixel in the grid, with adjusted input parameters
for y in range(height):
    for x in range(width):
        scale_factor = 50
        frequency_factor = 10

        noise_r   = int(255 * noise.snoise2((x+30)/50 , y/scale_factor , octaves=6, persistence=0.5, lacunarity=1.2, repeatx=width, repeaty=height))
        noise_g   = int(255 * noise.snoise2((x+90)/60 , y/scale_factor , octaves=5, persistence=0.9, lacunarity=1.5, repeatx=width, repeaty=height))
        noise_b   = int(255 * noise.snoise2((x-50)/70 , y/scale_factor , octaves=4, persistence=1.2, lacunarity=1.8, repeatx=width, repeaty=height))

        img.putpixel((x, y), (noise_r, noise_g, noise_b))

img.show()
