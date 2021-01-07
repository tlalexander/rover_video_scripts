import os
import subprocess as sp

VIDEO_DIRECTORY='/media/taylor/curie/spherical/mountain_bike/section2'

# INPUT1='GPBK4842.MP4'
# INPUT2='GPFR4842.MP4'

INPUT1='GPBK5475.MP4'
INPUT2='GPFR5475.MP4'
OUTPUT='out.mp4'

#sys.exit()


filename1 = os.path.join(VIDEO_DIRECTORY, INPUT1)
filename2 = os.path.join(VIDEO_DIRECTORY, INPUT2)
output = os.path.join(VIDEO_DIRECTORY, OUTPUT)


command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {} -hwaccel cuvid -c:v h264_cuvid -i {} ".format(filename1, filename2) +
"-filter_complex '[0:v] hwdownload, format=nv12 [left]; [1:v] hwdownload, format=nv12 [right]; [left][right]hstack=inputs=2[mosaic]; [mosaic] hwupload_cuda' " +
"-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 140M -maxrate:v 160M -c:a aac -b:a 240k {}".format(output))
print("Running command: {}".format(command))
try:
    output = sp.check_output(command, shell=True)
except sp.CalledProcessError as e:
    print("Error with video {}. Proceeding to the next. Actual error was:")
    print(e)
print("Output was: {}".format(output))
