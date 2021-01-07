import numpy as np
import cv2
import glob
import argparse




# Intrinsic_mtx_1 [[3.31481153e+03 0.00000000e+00 1.75479058e+03]
#  [0.00000000e+00 3.16055105e+03 1.03984724e+03]
#  [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
# dist_1 [[-0.20507495  0.102486    0.00409406 -0.03564857 -0.01609875]]
# Intrinsic_mtx_2 [[7.21320876e+03 0.00000000e+00 1.96421967e+03]
#  [0.00000000e+00 7.88926434e+03 9.90116526e+02]
#  [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
# dist_2 [[ 2.19387586e+00 -2.27186777e+01  6.33705225e-02  4.49409793e-02
#    9.39999737e+01]]
# R [[ 0.73666657  0.01266957 -0.67613745]
#  [ 0.09023695  0.98904189  0.11684795]
#  [ 0.67020867 -0.14709056  0.72745083]]
# T [[-21.55524523]
#  [-10.17276181]
#  [112.08026599]]
# E [[ -16.93165412 -109.35576039  -20.49653305]
#  [  97.01229729   -1.75056473  -60.10128384]
#  [   5.54885403  -21.19015591   -9.39687136]]
# F [[-3.73390343e-07 -2.52930610e-06  1.78699946e-03]
#  [ 1.95606137e-06 -3.70194442e-08 -7.41095063e-03]
#  [-3.20643865e-04  1.46949804e-03  1.00000000e+00]]




class StereoCalibration(object):
    def __init__(self, filepath):
        # termination criteria
        self.criteria = (cv2.TERM_CRITERIA_EPS +
                         cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.criteria_cal = (cv2.TERM_CRITERIA_EPS +
                             cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-5)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        self.objp = np.zeros((9*6, 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

        # Arrays to store object points and image points from all the images.
        self.objpoints = []  # 3d point in real world space
        self.imgpoints_l = []  # 2d points in image plane.

        self.cal_path = filepath
        self.read_images(self.cal_path)

    def read_images(self, cal_path):
        images_left = glob.glob(cal_path + '1_*.png')
        images_left.sort()
        print(len(images_left))

        for i, fname in enumerate(images_left):
            img_l = cv2.imread(images_left[i])

            gray_l = cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret_l, corners_l = cv2.findChessboardCorners(gray_l, (9, 6), None)


            if ret_l is True and ret_r is True:

                # If found, add object points, image points (after refining them)
                self.objpoints.append(self.objp)

                rt = cv2.cornerSubPix(gray_l, corners_l, (11, 11),
                                      (-1, -1), self.criteria)
                self.imgpoints_l.append(corners_l)

                # Draw and display the corners
                ret_l = cv2.drawChessboardCorners(img_l, (9, 6),
                                                  corners_l, ret_l)
                print(images_left[i])
                #print(images_left[i].replace("/cal", "/cal/out"))
                #cv2.imwrite(images_left[i].replace("/cal", "/cal/out"), img_l)
                #cv2.imshow(images_left[i], img_l)
                #cv2.waitKey(500)

            # if ret_r is True:


                #cv2.imwrite(images_right[i].replace("/cal", "/cal/out"), img_r)
                #cv2.imshow(images_right[i], img_r)
                #cv2.waitKey(500)
            img_shape = gray_l.shape[::-1]

        print("{}. {}, {}".format(len(self.objpoints), len(self.imgpoints_l), len(self.imgpoints_r)))

        rt, self.M1, self.d1, self.r1, self.t1 = cv2.calibrateCamera(
            self.objpoints, self.imgpoints_l, img_shape, None, None)

        newcameramtx, roi = cv.getOptimalNewCameraMatrix(self.M1, self.d1, img_shape, 1, img_shape)

        for i, fname in enumerate(images_left):
            img = cv2.imread(images_left[i])

            # img = cv.imread('left12.jpg')
            dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
            cv2.imshow("image", dst)
            cv2.waitKey(500)

        self.camera_model = self.stereo_calibrate(img_shape)

    def stereo_calibrate(self, dims):
        flags = 0
        flags |= cv2.CALIB_FIX_INTRINSIC
        # flags |= cv2.CALIB_FIX_PRINCIPAL_POINT
        flags |= cv2.CALIB_USE_INTRINSIC_GUESS
        flags |= cv2.CALIB_FIX_FOCAL_LENGTH
        # flags |= cv2.CALIB_FIX_ASPECT_RATIO
        flags |= cv2.CALIB_ZERO_TANGENT_DIST
        # flags |= cv2.CALIB_RATIONAL_MODEL
        # flags |= cv2.CALIB_SAME_FOCAL_LENGTH
        # flags |= cv2.CALIB_FIX_K3
        # flags |= cv2.CALIB_FIX_K4
        # flags |= cv2.CALIB_FIX_K5

        stereocalib_criteria = (cv2.TERM_CRITERIA_MAX_ITER +
                                cv2.TERM_CRITERIA_EPS, 100, 1e-5)
        ret, M1, d1, M2, d2, R, T, E, F = cv2.stereoCalibrate(
            self.objpoints, self.imgpoints_l,
            self.imgpoints_r, self.M1, self.d1, self.M2,
            self.d2, dims,
            criteria=stereocalib_criteria, flags=flags)

        print('Intrinsic_mtx_1', M1)
        print('dist_1', d1)
        print('Intrinsic_mtx_2', M2)
        print('dist_2', d2)
        print('R', R)
        print('T', T)
        print('E', E)
        print('F', F)

        # for i in range(len(self.r1)):
        #     print("--- pose[", i+1, "] ---")
        #     self.ext1, _ = cv2.Rodrigues(self.r1[i])
        #     self.ext2, _ = cv2.Rodrigues(self.r2[i])
        #     print('Ext1', self.ext1)
        #     print('Ext2', self.ext2)

        print('')

        camera_model = dict([('M1', M1), ('M2', M2), ('dist1', d1),
                            ('dist2', d2), ('rvecs1', self.r1),
                            ('rvecs2', self.r2), ('R', R), ('T', T),
                            ('E', E), ('F', F)])

        cv2.destroyAllWindows()
        return camera_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='String Filepath')
    args = parser.parse_args()
    cal_data = StereoCalibration(args.filepath)
