
#
# cp  IMAGE_SOURCE ${BASE_DIR}/images/


import shutil
import os

IMAGE_SOURCE="/media/taylor/external/Rover/rover_software/coco-annotator/datasets/rover_singles/images"

IMAGE_DESTINATION="/media/taylor/external/Rover/tlt_workspace/rover_data_18/images"

extensions = [".jpg", ".jpeg", ".png", ".PNG"]

for root, dirs, files in os.walk(IMAGE_SOURCE, topdown=False):
    dirs[:] = [d for d in dirs if not d[0] == '.']
    for name in files:
        filename, file_extension = os.path.splitext(name)
        if file_extension in extensions:
            source = os.path.join(root, name)
            print(source)
            shutil.copy(source, IMAGE_DESTINATION)