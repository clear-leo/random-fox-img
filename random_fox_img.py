import requests
from PIL import Image

response = requests.get("https://randomfox.ca/floof/")


fox = response.json()
fox_img = requests.get(fox["image"])
with open("fox.jpg", "wb") as handler:
    handler.write(fox_img.content)

im = Image.open("fox.jpg")
im.show()
