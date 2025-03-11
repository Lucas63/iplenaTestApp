import base64
from io import BytesIO

from PIL import Image


def base64_to_image(base64_string):
    image_data = base64.b64decode(base64_string)  # Decode the base64 string
    image = Image.open(BytesIO(image_data))  # Convert binary data to an image
    return image