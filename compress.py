#Compress image files using PILLOW library

from PIL import Image
import PIL
import os
import glob

def compress_images(directory=False, quality=30):
    # 1. If there is a directory then change into it, else perform the next operations inside of the 
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png', 'jpeg', 'JPG'))]
    # print(f" Example images: {images}")


    # 4. Loop over every image:
    for image in images:
        print(image)
        # 5. Open every image:
        img = Image.open(image)
        # 5. Compress every image and save it with a new name:
        img.save("smaller_"+image, optimize=True, quality=quality)
    
list_of_folders = ['1 Market', '2 Product and price', '3 Silviculture', '4 Improve scale', '5 Risk', 'Algemeen']

folder_number = 2

folder_to_process = os.getcwd() + "\\" + list_of_folders[folder_number]
print("Processing images in " + folder_to_process)    
compress_images(folder_to_process)




