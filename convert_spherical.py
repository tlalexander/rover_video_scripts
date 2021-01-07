import os
import subprocess as sp

WORKING_DIRECTORY = "/media/taylor/external/Software/rover_jetson/vrworks/package/samples/nvstitch_sample"
LD_LIBRARY_PATH = "../../nvcalib/binary;../../nvstitch/binary;../../external/cuda;../../external/fdkaac;../../external/opencv-3.4.2/binary"

input_dir_base = "/media/taylor/curie/spherical/long_trail_day/section"


command = "LD_LIBRARY_PATH=\"../../nvcalib/binary;../../nvstitch/binary;../../external/cuda;../../external/fdkaac;../../external/opencv-3.4.2/binary\" && " + \
"export LD_LIBRARY_PATH && " + \
"./nvstitch_sample --input_dir_base {} --video_input video.xml ".format(input_dir_base) + \
"--stitcher_spec stitcher_spec.xml --rig_spec out_calib.xml --inject_metadata 1" + \
" --audio --audio_rig_spec audio_rig_spec.xml --audio_input audio_rig_spec.xml"


sp.Popen(command, cwd=WORKING_DIRECTORY, shell=True)