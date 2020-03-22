import pytesseract as pt
import os

# os.path()
from PIL import Image
#生成图片实例
image = Image.open(r"C:\Users\lenovo1\untitled\image\testOCR.jpg")
#调用pytesseract,把图片转换为文字
text = pt.image_to_string(image)
print(text)

