from PIL import Image

img = Image.open('./img/right.jpg')

box = (375, 175, 800, 1050)
img2 = img.crop(box)

img2.show()
img2.save('./img/output.jpg')