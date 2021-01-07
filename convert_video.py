import os
import subprocess as sp


"""batch convert videos to a 4x4 720p version"""


#VIDEO_DIRECTORY = '/media/taylor/external/robot/Rover/trail'
#VIDEO_DIRECTORY = '/media/taylor/feynman/rover_videos/trail_scan/Videos'
VIDEO_DIRECTORY = '/media/taylor/external/robot/Rover/trail/unprocessed'




video_groups = []


#{01_20_2020_20:49:06}_


files = os.listdir(VIDEO_DIRECTORY)
print(files)




idx = 0
for file in files:
    match = False
    for video in video_groups:
        if video[:21] == file[:21]:
            match = True
            print('Match: {} {}'.format(video[:21], file[:21]))
    if not match:
        video_groups.append(files[idx])
        idx+=1
print(video_groups)

#sys.exit()

for video in video_groups:
    filename = os.path.join(VIDEO_DIRECTORY, video[:21])
    output = "{}_merged".format(video[:21])
    output = os.path.join(VIDEO_DIRECTORY, output)

    if os.path.isfile("{}_720.mp4".format(output)):
        print("Output file already exists and will be skipped: {}".format(output))
    else:
        #command = "ffmpeg -i {}_2.mkv -i {}_4.mkv -i {}_3.mkv -i {}_1.mkv -filter_complex '[0:v][1:v]hstack=inputs=2[top];[2:v][3:v]hstack=inputs=2[bottom];[top][bottom]vstack=inputs=2[v]' -vsync 0 -map '[v]' {}.mp4".format(filename,filename,filename,filename,output)

        command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_4.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_3.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_1.mkv ".format(filename,filename,filename,filename) +
        "-filter_complex '[0:v] scale_npp=1280:720, hwdownload, format=nv12 [upperleft]; [1:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerleft]; [2:v] scale_npp=1280:720, hwdownload, format=nv12 [upperright]; " +
        "[3:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerright]; [upperleft][upperright][lowerleft][lowerright]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[mosaic]; [mosaic] hwupload_cuda' " +
        "-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}_720.mp4".format(output))

        # command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v hevc_cuvid -i {}_1.mp4 -hwaccel cuvid -c:v hevc_cuvid -i {}_3.mp4 -hwaccel cuvid -c:v hevc_cuvid -i {}_2.mp4 -hwaccel cuvid -c:v hevc_cuvid -i {}_0.mp4 ".format(filename,filename,filename,filename) +
        # "-filter_complex '[0:v] scale_npp=1280:720, hwdownload, format=nv12 [upperleft]; [1:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerleft]; [2:v] scale_npp=1280:720, hwdownload, format=nv12 [upperright]; " +
        # "[3:v] scale_npp=1280:720, hwdownload, format=nv12 [lowerright]; [upperleft][upperright][lowerleft][lowerright]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[mosaic]; [mosaic] hwupload_cuda' " +
        # "-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}_720.mp4".format(output))

        # command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_4.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_3.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_1.mkv ".format(filename,filename,filename,filename) +
        # "-filter_complex '[0:v] hwdownload, format=nv12 [upperleft]; [1:v] hwdownload, format=nv12 [lowerleft]; [2:v] hwdownload, format=nv12 [upperright]; " +
        # "[3:v] hwdownload, format=nv12 [lowerright]; [upperleft][upperright][lowerleft][lowerright]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[mosaic]; [mosaic] hwupload_cuda' " +
        # "-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}.mp4".format(output))
        print("Running command: {}".format(command))
        try:
            output = sp.check_output(command, shell=True)
        except sp.CalledProcessError as e:
            print("Error with video {}. Proceeding to the next. Actual error was:")
            print(e)
        print("Output was: {}".format(output))
