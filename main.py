import cv2
from PIL import Image
import pytesseract


#---------libs


im1_file = "data/image/data1.png" #sourcing the image from folder

im1 = Image.open(im1_file) # using pillow to present the image in the lib

print(im1)
im1.show() # to show the image directly
im1.rotate(90).show() # to rotate the image

im1.save("temp/data1.png") # saving the image in different folder

