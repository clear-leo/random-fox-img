import requests
from PIL import Image
import io

response = requests.get("https://randomfox.ca/floof/")

fox = response.json()
fox_img = requests.get(fox["image"]).content

im = Image.open(io.BytesIO(fox_img))
im.show()
