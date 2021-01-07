

import subprocess


INPUT_VIDEO_PATH = "/media/taylor/external/Rover/tlt_workspace/output6.mp4"


res_command = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 {}".format(INPUT_VIDEO_PATH)

out = subprocess.run(res_command, shell=True, capture_output=True, encoding='utf-8').stdout

width, height = out.strip().split(',')
width = int(width)
height = int(height)
# import sys
# sys.exit()

command_2 = "ffmpeg -i {} -filter:v \"crop={}:{}:{}:{}\" {}".format(INPUT_VIDEO_PATH, width/2, height/2, 0, 0, "out_2.mp4")
command_0 = "ffmpeg -i {} -filter:v \"crop={}:{}:{}:{}\" {}".format(INPUT_VIDEO_PATH, width/2, height/2, width/2+1, 0, "out_0.mp4")
command_1 = "ffmpeg -i {} -filter:v \"crop={}:{}:{}:{}\" {}".format(INPUT_VIDEO_PATH, width/2, height/2, 0, height/2+1, "out_1.mp4")
command_3 = "ffmpeg -i {} -filter:v \"crop={}:{}:{}:{}\" {}".format(INPUT_VIDEO_PATH, width/2, height/2, width/2+1, height/2+1, "out_3.mp4")

for command in [command_0, command_1, command_2, command_3]:
    print(command)
    subprocess.run(command, shell=True)