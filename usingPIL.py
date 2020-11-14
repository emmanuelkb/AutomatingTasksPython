#!/usr/bin/env python3

import os
from PIL import Image 

directory = r'C:/Users/emmanuel_kb/Pictures/Saved Pictures/' #Store directory
for filename in os.listdir(directory):                       #iterate through files in directory 
    if filename.endswith(".png"):                            # Select only files with png extension
        image = Image.open(directory + filename).convert('RGB') #open image and store in image variable
       	print("image opened")
        path, file = os.path.split(filename)                 #Split path into path and file
        file = os.path.splitext(file)[0]                     #split file into name and extension and select name
        image.rotate(270).resize((128,128)).save('C:/Users/emmanuel_kb/Pictures/Saved Pictures/{}.jpeg'.format(file))
                                                             #rename with old name and .jpeg extension
        print('Image done')
    else:

        continue

print('Operation done')