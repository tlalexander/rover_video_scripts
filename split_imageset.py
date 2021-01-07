import os
from image_slicer import slice

# Chops images from 2x2 grid to individual images

base_dirs = ['/media/taylor/jemison/datasets/rover/images',
             '/media/taylor/jemison/datasets/rover/annotations']

file_list = []

for directory in base_dirs:
    for (dirpath, dirnames, filenames) in os.walk(directory):
        files = [os.path.join(dirpath, filename) for filename in filenames]
        for file in files:
            file_list.append(file)

for file in file_list:
    directory, filename = os.path.split(file)
    if file[-3:] == 'png':
        os.chdir(directory)
        slice(file, 4)
        os.remove(file)
    print(file)
