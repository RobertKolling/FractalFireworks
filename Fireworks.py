import random
from PIL import Image
import noise

# Image size (width, height)
size = (800, 600)

# Create a new image with a black background
img = Image.new("RGB", size, (0, 0, 0))
pixels = img.load()

# Fractal noise parameters
octaves = 6
persistence = 0.5
lacunarity = 2.0

# Generate fractal noise
for x in range(img.width):
    for y in range(img.height):
        value = noise.pnoise3(x/100, y/100, octaves, persistence, lacunarity)
        value = (value + 1) / 2
        r = int(random.random() * 255 * value)
        g = int(random.random() * 255 * value)
        b = int(random.random() * 255 * value)
        pixels[x, y] = (r, g, b)

# Save the image
img.save("fractal_fireworks.png")
