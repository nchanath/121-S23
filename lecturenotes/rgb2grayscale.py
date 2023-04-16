from PIL import Image

# Open the RGB image
rgb_image = Image.open("bird.jpg")

# Get the size of the image
width, height = rgb_image.size

# Create a new grayscale image with the same size as the RGB image
grayscale_image = Image.new("L", (width, height))

# Convert each pixel of the RGB image to grayscale by averaging its RGB values using nested for loops
for x in range(width):
    for y in range(height):
        r, g, b = rgb_image.getpixel((x, y))
        gray = int((r + g + b) / 3)
        grayscale_image.putpixel((x, y), gray)

# Save the grayscale image
grayscale_image.save("bird-gray.jpg")
