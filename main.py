from PIL import Image, ImageOps

def invert_image(input_path, output_path):
    image = Image.open(input_path).convert("RGB")  # Ensure image is in RGB mode
    inverted_image = ImageOps.invert(image)
    inverted_image.save(output_path)

# Example usage
invert_image("PLEASANT_.jpg", "output.jpg")
