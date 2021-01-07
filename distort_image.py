import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

IMAGE_H = 720
IMAGE_W = 1280

X1 = 600
Y1 = 600
# END_W = 20
# END_H = -50
END_W = 100
END_H = -100
dst = np.float32([[X1, Y1], [X1 + END_W, Y1], [X1 + END_W, Y1 - END_H], [X1, Y1 - END_H]])

X1 = 600
Y1 = 400
# END_W = 20
# END_H = -50
SHIFT = 10
END_W = 80
END_H = -45
dst2 = np.float32([[X1+SHIFT, Y1], [X1 + END_W + SHIFT, Y1], [X1 + END_W, Y1 - END_H], [X1, Y1 - END_H]])
print(dst)
print(dst2)


# 1061, 423
# 1149, 413
# 1175, 437
# 1067, 448

# 796, 317
# 861, 310
# 881, 327
# 801, 336

# 748, 438
# 1071, 420
# 1159, 487
# 649, 504


#right
# 176, 442
# 474, 427
# 639, 511
# 194, 563

#
# 242, 413
# 869, 331
# 1149, 354
# 592, 610

#[99,379],[239, 381],[242, 392],[92, 389]




# parking = np.float32([[1688, 1188],[2267, 1218],[2959, 1479],[1318, 1313]])
# parking = np.float32([[426, 1371],[1415,1330],[1938,1438],[195, 1576]])
parking = np.float32([[892, 1336],[1953, 1264],[3049, 1383],[1330, 1804]])
parking = np.float32([[1613, 1366],[2663, 1388],[1948, 1825],[584, 1505]])





IMAGE_H = 2160
IMAGE_W = 3840
X1 = 1600
Y1 = 1400
# END_W = 20
# END_H = -50
SHIFT = 0
END_W = 400
END_H = -400
dst_parking = np.float32([[X1, Y1 + SHIFT], [X1 + END_W, Y1], [X1 + END_W, Y1 - END_H], [X1, Y1 - END_H + SHIFT]])
M_parking = cv2.getPerspectiveTransform(parking, dst_parking) # The transformation matrix


src = np.float32([[1061+5, 423], [1149, 413], [1175, 437], [1067, 448]])


left_new = np.float32([[748, 438],[1071, 420],[1159, 487],[649, 504]])
right_new = np.float32([[176, 442],[474, 427],[639, 511],[194, 563]])
# src4 = np.float32([[242, 413],[869, 331],[1149, 354],[592, 610]])

#right_new = np.float32([[92, 333],[233, 333],[234, 381],[82, 381]])
# right_new = np.float32([[99,379],[239, 381],[242, 392],[92, 389]])
#src = np.float32([[796, 317], [861, 310], [881, 327], [801, 336]])
# dst = np.float32([[X1, Y1], [X1 + END_W, Y1], [X1 + END_W, Y1 - END_H], [X1, Y1 - END_H]])
M_left = cv2.getPerspectiveTransform(left_new, dst) # The transformation matrix
M_right = cv2.getPerspectiveTransform(right_new, dst2) # The transformation matrix

#img = cv2.imread('sample_distort_frame.png') # Read the test img
#img = cv2.imread('capture.png') # Read the test img
#img = cv2.imread('out/l_493.jpeg') # Read the test img
#img = cv2.imread('out/r_493.jpeg') # Read the test img
img1 = cv2.imread('left_sample.png') # Read the test img
img2 = cv2.imread('right_sample2.png') # Read the test img
# img_parking = cv2.imread('/media/taylor/external/robot/Rover/trail/homography/frames/out/cam_3/{12_05_2020_15:35:36}_3_003.png') # Read the test img
img_parking = cv2.imread('/media/taylor/external/robot/Rover/trail/homography/frames/out/cam_0/{12_05_2020_15:35:36}_0_037.png') # Read the test img
img_parking = cv2.imread('/media/taylor/external/robot/Rover/trail/homography/frames/out/cam_2/{12_05_2020_15:35:36}_2_037.png') # Read the test img
# img_parking = cv2.imread('/media/taylor/external/robot/Rover/trail/homography/frames/out/cam_1/{12_05_2020_15:35:36}_1_003.png') # Read the test img
#img = cv2.imread("/media/taylor/external/robot/Rover/stereo_calibration/video/00/009.bmp")
#img = cv2.imread('left_sample.png') # Read the test img
#img = cv2.imread('left.png') # Read the test img
# M = cv2.getRotationMatrix2D((0, 0), 25, 1)
#warped_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
#img = img[450:(450+IMAGE_H), 0:IMAGE_W] # Apply np slicing for ROI crop
#warped_img1 = cv2.warpPerspective(img1, M_left, (IMAGE_W, IMAGE_H)) # Image warping
#warped_img2 = cv2.warpPerspective(img2, M_right, (IMAGE_W, IMAGE_H)) # Image warping
warped_img_parking = cv2.warpPerspective(img_parking, M_parking, (IMAGE_W, IMAGE_H)) # Image warping
#plt.imshow(cv2.cvtColor(warped_img1, cv2.COLOR_BGR2RGB)) # Show results
plt.imshow(cv2.cvtColor(warped_img_parking, cv2.COLOR_BGR2RGB)) # Show results
plt.show()