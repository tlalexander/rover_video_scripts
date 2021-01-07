import sys
import subprocess


ANNOTATIONS_PATH = "/media/taylor/external/Rover/rover_software/coco-annotator/datasets/rover_singles/rover_singles-9.json"

TRAIN_PATH = "/media/taylor/external/Rover/tlt_workspace/rover_data_18/rover_train_annotations.json"
TEST_PATH = "/media/taylor/external/Rover/tlt_workspace/rover_data_18/rover_test_annotations.json"

COCO_SPLIT= "/media/taylor/external/Rover/rover_software/cocosplit/cocosplit.py"

SPLIT = "0.8"

command = ["python3", COCO_SPLIT, "-s", SPLIT, ANNOTATIONS_PATH, TRAIN_PATH, TEST_PATH, "--having-annotations"]

string_command = ' '.join(command)

print(string_command)

subprocess.run(command)