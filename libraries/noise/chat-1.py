import noise
from PIL import Image

# Set the size of the grid
width, height = 71, 46

# Create a new grayscale image with the specified size
img = Image.new('L', (width, height))

# Generate Perlin noise for each pixel in the grid
for y in range(height):
    for x in range(width):
        noise_val = int(255 * noise.snoise2(x/300, y/300, octaves=4, persistence=0.5, lacunarity=1.2, repeatx=width, repeaty=height))
        img.putpixel((x, y), noise_val)

img.show()
