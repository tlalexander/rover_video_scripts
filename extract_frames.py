import os
import subprocess as sp


# VIDEO_DIRECTORY = '/media/taylor/external/robot/Rover/trail/extract'
# VIDEO_DIRECTORY = '/media/taylor/jemison/Photography2020/fisheye'

VIDEO_DIRECTORY = '/media/taylor/external/Rover/trail/panasonic/cctag_trail/small_cluster'

OUTPUT_DIRECTORY = '/media/taylor/external/Rover/trail/panasonic/cctag_trail/small_cluster'

VIDEO_DIRECTORY = '/home/taylor/Documents/acorn_video'

OUTPUT_DIRECTORY = VIDEO_DIRECTORY


start_time_sec = 0
end_time_sec = 1000
rate = 15

duration = end_time_sec - start_time_sec

video_files = []

JPG_EXT = ".jpg"
PNG_EXT = ".png"
OUTPUT_FORMAT = PNG_EXT


USE_MESHROOM_RIG_FOLDER_FORMAT = False


#{01_20_2020_20:49:06}_


files = os.listdir(VIDEO_DIRECTORY)
print(files)


#date_number = int(file_name.replace(".png", "").replace('converted_', ''))
#print(date_number)





for file in files:
    if "mkv" in file or "mp4" in file or "MP4" in file:
        video_files.append(file)
print(video_files)


for video in video_files:
    filename = os.path.join(VIDEO_DIRECTORY, video)
    base_name = video.split('.mp4')[0].split('.mkv')[0].split('.MP4')[0]
    if USE_MESHROOM_RIG_FOLDER_FORMAT:
        base_name_full = os.path.join(OUTPUT_DIRECTORY,"rig", base_name[-1:],"%03d{}".format(OUTPUT_FORMAT))
    else:
        base_name_full = os.path.join(OUTPUT_DIRECTORY, 'frames', base_name, base_name)
        base_name_full = "{}_%03d{}".format(base_name_full, OUTPUT_FORMAT)
    format_options = ""
    if OUTPUT_FORMAT == JPG_EXT:
        format_options = "-qscale:v 1 -qmin 1"
    if OUTPUT_FORMAT == PNG_EXT:
        pass
        #format_options = "-vf scale=3000x2250 -pix_fmt bgr8"
    print(base_name_full)
    print(os.path.dirname(base_name_full))
    if not os.path.exists(os.path.dirname(base_name_full)):
       os.makedirs(os.path.dirname(base_name_full))
    command = ("ffmpeg -ss {} -t {} -i {} -r {} {} {}".format(start_time_sec, duration, filename, rate, format_options, base_name_full))
    print("Running command: {}".format(command))
    output = sp.check_output(command, shell=True)
    print("Output was: {}".format(output))
    # if OUTPUT_FORMAT == JPG_EXT:
    #     exif_dict = piexif.load(output_file_name)
    #     exif_dict['Exif'][piexif.ExifIFD.BodySerialNumber] =  bytes('00{}'.format(rig_index), 'utf-8')
    #     exif_dict['Exif'][piexif.ExifIFD.FocalLength] = (3,1)
    #     exif_dict['0th'][piexif.ImageIFD.Make] = bytes('GoPro', 'utf-8')
    #     exif_dict['0th'][piexif.ImageIFD.Model] = bytes('FUSION', 'utf-8')
    #     exif_dict['0th'][piexif.ImageIFD.DateTime] = bytes('2020:01:01 01:00:{:02d}'.format(date_number), 'utf-8')
    #     exif_bytes = piexif.dump(exif_dict)
    #     piexif.insert(exif_bytes, output_file_name)
