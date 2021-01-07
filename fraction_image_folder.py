import os
import shutil

source_folder_name = "/media/taylor/curie/drone_footage/sample_dense"
target_folder_name = "/media/taylor/curie/drone_footage/sample_fractioned"

files = os.listdir(source_folder_name)
files.sort()
print(files)

RESET = 0

copy_divisor = 2
count = RESET

for file in files:
    if ".png" or ".jpg" in file:
        count += 1
        if count == copy_divisor:
            count = RESET
            print("Copying {}".format(file))
            file = os.path.join(source_folder_name, file)
            shutil.copy2(file, target_folder_name)

