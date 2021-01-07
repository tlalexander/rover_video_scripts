import numpy as np
import cv2
import time


def convert_frame(cv_frame, shift, homography):
    # parking = np.float32([[426, 1371],[955, 1354],[1207, 1514],[195, 1576]])

    IMAGE_W = 3840
    IMAGE_H = 2160

    y1=1000
    y2=1460
    x1=500
    x2=1500

    X1 = 895
    Y1 = 1200
    # END_W = 20
    # END_H = -50
    SHIFT = shift
    END_W = 200
    END_H = -200
    dst_parking = np.float32([[X1, Y1 + SHIFT], [X1 + END_W, Y1], [X1 + END_W, Y1 - END_H], [X1, Y1 - END_H + SHIFT]])
    M_parking = cv2.getPerspectiveTransform(homography, dst_parking) # The transformation matrix
    warped_img_parking = cv2.warpPerspective(cv_frame, M_parking, (IMAGE_W, IMAGE_H)) # Image warping
    #return warped_img_parking
    roi = warped_img_parking[y1:y2, x1:x2]
    return roi


def smart_add(frame, frame2):
    ret, frame3 = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY);
    frame3 = cv2.bitwise_not(frame3)
    ret, frame4 = cv2.threshold(frame2, 0, 255, cv2.THRESH_BINARY);
    frame4 = cv2.bitwise_not(frame4)
    #dst = cv2.addWeighted(frame, 0.5, frame2, 0.5, 0.0)
    #dst = cv2.addWeighted(frame, 1, frame2, 1, 0.0)
    mask = cv2.add(frame4, frame3)
    #mask = cv2.add(mask, frame3)
    dst = cv2.addWeighted(frame, 1, frame2, 1, 0.0)
    dst2 = cv2.addWeighted(frame, 0.5, frame2, 0.5, 0.0)

    dst2 = cv2.subtract(dst2, mask)
    dst = cv2.subtract(dst, cv2.bitwise_not(mask))

    #ret, frame3 = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY);
    dst = cv2.add(dst, dst2)
    return dst


def offset_left_right(frame, frame2, angle, height_offset, width_offset):
    height, width, channels = frame.shape
    degrees = angle
    center  = (width/2.0, height/1.0)
    # translate
    M = np.float32([[1,0,width_offset],[0,1,height_offset]])
    frame = cv2.warpAffine(frame,M,(width,height))

    # translate
    M = np.float32([[1,0,-width_offset],[0,1,-height_offset]])
    frame2 = cv2.warpAffine(frame2,M,(width,height))

    # rotate
    # mat = cv2.getRotationMatrix2D(center, degrees, 1.0)
    mat = cv2.getRotationMatrix2D(center, 0.0, 1.0)
    frame  = cv2.warpAffine(frame, mat, (width, height))

    mat2 = cv2.getRotationMatrix2D(center, 0.0-degrees, 1.0)
    # mat2 = cv2.getRotationMatrix2D(center, 0.0, 1.0)
    frame2  = cv2.warpAffine(frame2, mat2, (width, height))
    return frame, frame2

def rotate_about_center(frame, degrees=180):
    height, width, channels = frame.shape
    center  = (width/2.0, height/1.0)
    # rotate
    mat = cv2.getRotationMatrix2D(center, degrees, 1.0)
    frame  = cv2.warpAffine(frame, mat, (width, height))
    return frame

# cap = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2020_00:58:10}_3.mp4_fixed-s1.mp4')
# cap2 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2020_00:58:10}_1.mp4_fixed-s1.mp4')
# cap3 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2020_00:58:10}_0.mp4_fixed-s1.mp4')
# cap4 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2020_00:58:10}_2.mp4_fixed-s1.mp4')
# # cap = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2020_00:58:13}_3.mp4')
# # cap2 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2020_00:58:13}_1.mp4')
# # cap = cv2.VideoCapture('/home/taylor/datasets/tlt_workspace/rover_data_18/rover/rover_sample8.mp4')
# # cap2 = cv2.VideoCapture('/home/taylor/datasets/tlt_workspace/rover_data_18/rover/rover_sample7.mp4')
#
# cap = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2019_14:35:12}_4.mkv')
# cap2 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2019_14:35:12}_2.mkv')
# cap3 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2019_14:35:12}_1.mkv')
# cap4 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_02_2019_14:35:12}_3.mkv')
#
# cap = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:35:36}_3.mp4')
# cap2 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:35:36}_1.mp4')
# cap3 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:35:36}_0.mp4')
# cap4 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:35:36}_2.mp4')
#
# cap = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:05:12}_3.mp4')
# cap2 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:05:12}_1.mp4')
# cap3 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:05:12}_0.mp4')
# cap4 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:05:12}_2.mp4')


cap = cv2.VideoCapture('/media/taylor/external/Rover/scripts/out_3.mp4')
cap2 = cv2.VideoCapture('/media/taylor/external/Rover/scripts/out_1.mp4')
cap3 = cv2.VideoCapture('/media/taylor/external/Rover/scripts/out_0.mp4')
cap4 = cv2.VideoCapture('/media/taylor/external/Rover/scripts/out_2.mp4')

#
#
# cap = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:23:45}_3.mp4')
# cap2 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:23:45}_1.mp4')
# cap3 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:23:45}_0.mp4')
# cap4 = cv2.VideoCapture('/media/taylor/external/robot/Rover/trail/unprocessed/{12_05_2020_15:23:45}_2.mp4')


FILEPATH = '/media/taylor/external/robot/Rover/trail/homography/frames/out/'

run=True
# width_offset = 0
# height_offset = 0
# angle = 30
# shift = -100
#
#
# width_offset = -7
# angle = -34
# shift = -125
# height_offset = 34

width_offset = 134
angle = 0
shift = 0
height_offset = 0


FRAME_START = 5000
# FRAME_START = 5
#FRAME_START = -1

#-14 -36 -131 9

old_frame = []
old_frame2 = []
old_frame3 = []
old_frame4 = []

frame3 = None
frame4 = None

use_masks = True
use_masks = False
mask_index = 1
mask_max = 716

lowres_input = False
lowres_input = True
height_768 = True

use_images = False

frame_index = 0


skip = [9,2,0,0]

for _ in range(skip[0]):
    cap.read()
for _ in range(skip[1]):
    cap2.read()
for _ in range(skip[2]):
    cap3.read()
for _ in range(skip[3]):
    cap4.read()

size = (3840, 2160)
ncc4 = cv2.VideoWriter_fourcc(*'MP4V')
output_video = cv2.VideoWriter("cv_out.mp4", ncc4, fps=9, frameSize=size, isColor=True)

while cap.isOpened() or use_images:
    if run:
        if use_images:
            print(FILEPATH + "cam_{}/{{12_05_2020_15:35:36}}_{}_{:03d}.png".format(3,3,mask_index))
            frame  = cv2.imread(FILEPATH + "cam_{}/{{12_05_2020_15:35:36}}_{}_{:03d}.png".format(3,3,mask_index))
            frame2 = cv2.imread(FILEPATH + "cam_{}/{{12_05_2020_15:35:36}}_{}_{:03d}.png".format(1,1,mask_index))
            frame3 = cv2.imread(FILEPATH + "cam_{}/{{12_05_2020_15:35:36}}_{}_{:03d}.png".format(0,0,mask_index))
            frame4 = cv2.imread(FILEPATH + "cam_{}/{{12_05_2020_15:35:36}}_{}_{:03d}.png".format(2,2,mask_index))
            mask_index+=1
        elif use_masks:
            if mask_index < mask_max:
                frame  = cv2.imread("out/r_{}.jpeg".format(mask_index))
                frame2 = cv2.imread("out/l_{}.jpeg".format(mask_index))
                mask_index+=1
            else:
                break
        else:
            ret, frame = cap.read()
            ret, frame2 = cap2.read()
            ret, frame3 = cap3.read()
            ret, frame4 = cap4.read()
            frame_index+=1
        # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
        old_frame = frame
        old_frame2 = frame2
        old_frame3 = frame3
        old_frame4 = frame4
    else:
        frame = old_frame
        frame2 = old_frame2
        frame3 = old_frame3
        frame4 = old_frame4

    if frame_index < FRAME_START:
        print("Skipping frame {}".format(frame_index))
        continue

    if lowres_input:
        if height_768:
            frame  = cv2.resize(frame,  (0, 0), fx=2.71875, fy=2.8125)
            frame2 = cv2.resize(frame2, (0, 0), fx=2.71875, fy=2.8125)
        else:
            frame  = cv2.resize(frame,  (0, 0), fx=2.71875, fy=3.0)
            frame2 = cv2.resize(frame2, (0, 0), fx=2.71875, fy=3.0)

    concat1 = np.concatenate((frame2, frame), axis=1)

    # cv2.imshow('frame', frame)
    # time.sleep(10)
    right_M = np.float32([[892, 1336],[1953, 1264],[3049, 1383],[1330, 1804]])
    left_M = np.float32([[1613, 1366],[2663, 1388],[1948, 1825],[584, 1505]])
    frame = convert_frame(frame, shift, right_M)
    frame2 = convert_frame(frame2, shift, left_M)
    frame, frame2 = offset_left_right(frame, frame2, angle, height_offset, width_offset)
    dst = smart_add(frame, frame2)


    try:

        if lowres_input:
            if height_768:
                frame3  = cv2.resize(frame3,  (0, 0), fx=2.71875, fy=2.8125)
                frame4 = cv2.resize(frame4, (0, 0), fx=2.71875, fy=2.8125)
            else:
                frame3  = cv2.resize(frame3,  (0, 0), fx=2.71875, fy=3.0)
                frame4 = cv2.resize(frame4, (0, 0), fx=2.71875, fy=3.0)

        concat2 = np.concatenate((frame4, frame3), axis=1)

        # left_M = np.float32([[1735, 1393],[2749, 1465],[2371, 1871],[753, 1515]])
        # right_M = np.float32([[425, 1371],[1415, 1330],[1940, 1437],[195, 1576]])
        frame3 = convert_frame(frame3, shift, right_M)
        frame4 = convert_frame(frame4, shift, left_M)

        frame3, frame4 = offset_left_right(frame3, frame4, angle, height_offset, width_offset)
        dst2 = smart_add(frame3, frame4)
        dst2 = cv2.rotate(dst2, cv2.ROTATE_180)
        dst = cv2.vconcat([dst, dst2])

        concat = np.concatenate((concat1, concat2), axis=0)
        concat = cv2.resize(concat, (0, 0), fx=0.264367816, fy=0.264367816)
        concat = cv2.copyMakeBorder(concat, 349, 349, 0, 0, cv2.BORDER_CONSTANT, (0,0,0))

        dst = cv2.resize(dst, (0, 0), fx=2.0, fy=2.0)

        dst = np.concatenate((concat, dst), axis=1)
        dst = cv2.copyMakeBorder(dst, 160, 160, 0, 0, cv2.BORDER_CONSTANT, (0,0,0))

        #print(concat.shape)
        #dst = dst2
    except Exception as e:
        print(e)
#    dst = cv2.add(dst, dst2)
    #frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    #dst = cv2.resize(dst, (0, 0), fx=1.5, fy=1.5)
    cv2.imshow('frame', dst)
    print(dst.shape)
    output_video.write(dst)
    #time.sleep(0.01)
    key = cv2.waitKey(1)
    if key == ord('q'):
        output_video.release()
        cv2.destroyAllWindows()
        break
    if key == ord(' '):
        print("toggle run")
        run=run==False
    if key == ord('a'):
        width_offset+=1
    if key == ord('d'):
        width_offset-=1
    if key == ord('j'):
        angle+=1
    if key == ord('l'):
        angle-=1
    if key == ord('i'):
        shift+=1
    if key == ord('k'):
        shift-=1
    if key == ord('w'):
        height_offset+=1
    if key == ord('s'):
        height_offset-=1
    # -7 -34 -125 34
    print(width_offset,angle, shift, height_offset)

cap.release()
cv2.destroyAllWindows()