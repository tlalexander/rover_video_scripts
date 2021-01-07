import os
import subprocess as sp
import shutil

NUM_IMAGES = 50
INPUT_DIRECTORY = '/home/taylor/datasets/tlt_workspace/rover_data_18/images'
OUTPUT_DIRECTORY = '/home/taylor/datasets/tlt_workspace/rover_data_18/images_val'


files = os.listdir(INPUT_DIRECTORY)
#print(files)


skip = round(len(files) / NUM_IMAGES)


for index in range(len(files)):
    if index % skip == 0:
        print(files[index])
        path = os.path.join(INPUT_DIRECTORY, files[index])
        shutil.copy(path, OUTPUT_DIRECTORY)





# for video in video_files:
#     filename = os.path.join(VIDEO_DIRECTORY, video)
#     base_name = video.split('.mp4')[0]
#     base_name_full = os.path.join(VIDEO_DIRECTORY, 'frames',base_name)
#     print(base_name_full)
#     if not os.path.exists(base_name_full):
#         os.makedirs(base_name_full)
#     #command = "ffmpeg -i {}_2.mkv -i {}_4.mkv -i {}_3.mkv -i {}_1.mkv -filter_complex '[0:v][1:v]hstack=inputs=2[top];[2:v][3:v]hstack=inputs=2[bottom];[top][bottom]vstack=inputs=2[v]' -vsync 0 -map '[v]' {}.mp4".format(filename,filename,filename,filename,output)
#     command = ("ffmpeg -i {} -r 1/1 {}/{}_%03d.png".format(filename, base_name_full,base_name))
#     # command = ("ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i {}_2.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_4.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_3.mkv -hwaccel cuvid -c:v h264_cuvid -i {}_1.mkv ".format(filename,filename,filename,filename) +
#     # "-filter_complex '[0:v] hwdownload, format=nv12 [upperleft]; [1:v] hwdownload, format=nv12 [lowerleft]; [2:v] hwdownload, format=nv12 [upperright]; " +
#     # "[3:v] hwdownload, format=nv12 [lowerright]; [upperleft][upperright][lowerleft][lowerright]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[mosaic]; [mosaic] hwupload_cuda' " +
#     # "-c:v hevc_nvenc -preset slow -rc vbr_hq -b:v 20M -maxrate:v 30M -c:a aac -b:a 240k {}.mp4".format(output))
#     print("Running command: {}".format(command))
#     output = sp.check_output(command, shell=True)
#     print("Output was: {}".format(output))
