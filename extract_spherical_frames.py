
import os
import subprocess as sp

import piexif


#ffmpeg -i converted_001.png -lavfi "v360=input=e:output=rectilinear:v_fov=90:yaw=180:pitch=45:h=2000:w=2000" -y rectilinear2.png


v_fov = 130
h_fov = 130
width = 2500
height = 2500

vertical_offset_degree = 30
horizontal_increments = 3
stagger_rows = True
ENABLE_TICK_TOCK = True


BASE_DIR = '/media/taylor/curie/spherical/foggy_day/section/frames'
OUTPUT_DIR = '/media/taylor/curie/spherical/foggy_day/section/'

USE_MESHROOM_RIG_FOLDER_FORMAT = True
EXPORT_JPG = True


command_list = []


files = os.listdir(BASE_DIR)
print(files)

image_files = []


for file in files:
    if "png" in file or "jpg" in file:
        image_files.append(file)
print(image_files)


format_options = ""

if ENABLE_TICK_TOCK:
    tick_tock = 1
else:
    tick_tock = 0

image_files.sort()

for file_name in image_files:
    tick_tock *= -1
    while True:
        for h_val in range(horizontal_increments):
            angle = int(360/horizontal_increments * h_val)
            if vertical_offset_degree < 0:
                angle += int(360.0/horizontal_increments/2)
            if tick_tock!= 0:
                angle += int(360.0/horizontal_increments/2) * tick_tock
            if angle > 180:
                angle = angle - 360
            #print(file_name.split(".png")[0])
            file_name_full_path = os.path.join(BASE_DIR, file_name)
            #print(output)
            if USE_MESHROOM_RIG_FOLDER_FORMAT:
                if vertical_offset_degree < 0:
                    rig_index = h_val + horizontal_increments
                else:
                    rig_index = h_val
                output_base = os.path.join(OUTPUT_DIR,"rig/{}".format(rig_index))
                output_file_name =  file_name
            else:
                output_file_name =  "{}_{}_{}.png".format(file_name.split(".png")[0], angle, vertical_offset_degree)
                output_base = OUTPUT_DIR
            if not os.path.exists(output_base):
                os.makedirs(output_base)
            output_file_name = os.path.join(output_base, output_file_name)
            if EXPORT_JPG:
                #output_file_name = output_file_name.replace(".png", ".jpg").replace('converted_', '0')
                output_file_name = output_file_name.replace(".png", ".jpg").replace('section_', '0')
                format_options = "-qscale:v 2"
            #print(OUTPUT_DIR)
        #    print(output)
            command = "ffmpeg -i {} -lavfi \"v360=input=e:output=rectilinear:v_fov={}:h_fov={}:yaw={}:pitch={}:h={}:w={}\" {} {}".format(file_name_full_path,v_fov,h_fov,angle,vertical_offset_degree,height,width,format_options,output_file_name)
            command_list.append(command)
            print("Running: {}".format(command))
            sp.check_output(command, shell=True)
            if USE_MESHROOM_RIG_FOLDER_FORMAT and EXPORT_JPG:


                if "png" in file_name:
                    date_number = int(file_name.replace(".png", "").replace('converted_', ''))
                else:
                    date_number = int(file_name.replace(".jpg", "").replace('section_', ''))
                print(date_number)

                exif_dict = piexif.load(output_file_name)
                exif_dict['Exif'][piexif.ExifIFD.BodySerialNumber] =  bytes('00{}'.format(rig_index), 'utf-8')
                exif_dict['Exif'][piexif.ExifIFD.FocalLength] = (3,1)
                exif_dict['0th'][piexif.ImageIFD.Make] = bytes('GoPro', 'utf-8')
                exif_dict['0th'][piexif.ImageIFD.Model] = bytes('FUSION', 'utf-8')
                exif_dict['0th'][piexif.ImageIFD.DateTime] = bytes('2020:01:01 01:00:{:02d}'.format(date_number), 'utf-8')
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, output_file_name)

            #print(command)
        if vertical_offset_degree > 0:
            vertical_offset_degree = -vertical_offset_degree
        else:
            vertical_offset_degree = abs(vertical_offset_degree)
            break


# print("Will run commands:")
# for item in command_list:
#     print(item)
#
# for item in command_list:
#     print("Running: {}".format(item))
#     output = sp.check_output(item, shell=True)