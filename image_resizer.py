from PIL import Image as img
import os
import glob
size_w, size_h = map(int, input('Please enter the desired size, for example 800 600 (width height): ').split(' '))
types = ['*.jpg', '*.jpeg', '*.png']
files_lst = []
for image_type in types:
    for x in glob.glob(image_type):
        files_lst.append(x)
for x in files_lst:
    current_image = img.open(x)
    new_image = current_image.resize((size_w, size_h))
    new_image.save(x)
