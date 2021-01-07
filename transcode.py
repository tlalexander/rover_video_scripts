import os
import subprocess as sp


# VIDEO_DIRECTORY = '/media/taylor/external/robot/Rover/trail/processed_sources'
#
#
# filename = os.path.join(VIDEO_DIRECTORY, 'out')
# output = "{}_merged".format('out')
# output = os.path.join(VIDEO_DIRECTORY, output)

filename = "/home/taylor/Software/openvslam/data/12mm_lens/PANA9172.MP4"
output =  "/home/taylor/Software/openvslam/data/12mm_lens/test1.mp4"


# command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}".format(filename) +
# " -c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}".format(output))
command = ("ffmpeg -vsync 0 -hwaccel cuvid -i {}".format(filename) +
" -c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 180M -maxrate:v 240M -c:a aac -b:a 240k {}".format(output))


# command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {} -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 ".format(filename) +
# " -c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k -shortest {}".format(output))

print("Running command: {}".format(command))
output = sp.check_output(command, shell=True)
print("Output was: {}".format(output))



"""
Using xstack filter:
https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos%20using%20xstack
Using h265 (required to support the extra resolution of 4x4k)
http://ntown.at/knowledgebase/cuda-gpu-accelerated-h264-h265-hevc-video-encoding-with-ffmpeg/
https://devblogs.nvidia.com/nvidia-ffmpeg-transcoding-guide/
"""