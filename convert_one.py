import os
import subprocess as sp


VIDEO_DIRECTORY = '/media/taylor/external/robot/Rover/trail/processed_sources'


filename = os.path.join(VIDEO_DIRECTORY, 'out')
output = "{}_merged".format('out')
output = os.path.join(VIDEO_DIRECTORY, output)
#command = "ffmpeg -i {}_2.mkv -i {}_4.mkv -i {}_3.mkv -i {}_1.mkv -filter_complex '[0:v][1:v]hstack=inputs=2[top];[2:v][3:v]hstack=inputs=2[bottom];[top][bottom]vstack=inputs=2[v]' -vsync 0 -crf 26 -map '[v]' {}_2.mp4".format(filename,filename,filename,filename,output)
#command = "ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -i {}_4.mkv -i {}_3.mkv -i {}_1.mkv -filter_complex '[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]' -map '[v]' -c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}_6.mp4".format(filename,filename,filename,filename,output)
# command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_4.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_3.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_1.mkv ".format(filename,filename,filename,filename) +
# "-filter_complex '[0:v] scale_npp=1280:720, hwdownload, format=nv12 [upperleft]; [1:v] scale_npp=1280:720, hwdownload, format=nv12 [upperright]; [2:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerleft]; " +
# "[3:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerright]; [upperleft][upperright] hstack [upperline]; [lowerleft][lowerright] hstack [lowerline]; [upperline][lowerline] vstack [mosaic]; [mosaic] hwupload_cuda' " +
# "-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}_7.mp4".format(output))
# command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_4.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_3.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_1.mkv ".format(filename,filename,filename,filename) +
# "-filter_complex '[0:v] scale_npp=1280:720, hwdownload, format=nv12 [upperleft]; [1:v] scale_npp=1280:720, hwdownload, format=nv12 [upperright]; [2:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerleft]; " +
# "[3:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerright]; [upperleft][upperright][lowerleft][lowerright]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[mosaic]; [mosaic] hwupload_cuda' " +
# "-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}_8.mp4".format(output))
command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_4.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_3.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_1.mkv ".format(filename,filename,filename,filename) +
"-filter_complex '[0:v] hwdownload, format=nv12 [upperleft]; [1:v] hwdownload, format=nv12 [upperright]; [2:v] hwdownload, format=nv12 [lowerleft]; " +
"[3:v] hwdownload, format=nv12 [lowerright]; [upperleft][upperright][lowerleft][lowerright]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[mosaic]; [mosaic] hwupload_cuda' " +
"-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}_9.mp4".format(output))
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