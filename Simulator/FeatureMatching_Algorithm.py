from Algorithm import Algorithm
import numpy as np
import cv2
import os

class FeatureMatching_Algorithm(Algorithm):
    def test(self, scanner_img, db_img):
        bs = scanner_img
        bd = db_img
        scanner_img = cv2.imread(scanner_img, cv2.IMREAD_GRAYSCALE)
        db_img = cv2.imread(db_img, cv2.IMREAD_GRAYSCALE)

        # Initiate SIFT detector
        sift = cv2.xfeatures2d.SIFT_create()
        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(scanner_img, None)
        kp2, des2 = sift.detectAndCompute(db_img, None)

        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]
        # ratio test as per Lowe's paper
        count = 0
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                count += 1
                matchesMask[i] = [1, 0]


        draw_params = dict(singlePointColor=(255, 0, 0),
                           matchesMask=matchesMask,
                           flags=cv2.DrawMatchesFlags_DEFAULT)
        img3 = cv2.drawMatchesKnn(scanner_img, kp1, db_img, kp2, matches, None, **draw_params)

        directory, filename = os.path.split(bd)

        # cv2.imwrite("F:\\ProjectRedHat\\FingerprintProject\\NormalizedCrossCor\\test\\featurematching\\" + filename, img3)
        if count > 200:
            return True
        else:
            return False

        # def test(self, scanner_img, db_img):
        #     scanner_img = cv2.imread(scanner_img, cv2.IMREAD_GRAYSCALE)
        #     db_img = cv2.imread(db_img, cv2.IMREAD_GRAYSCALE)
        #
        #     # Initiate ORB detector
        #     orb = cv2.ORB_create()
        #     # find the keypoints and descriptors with ORB
        #     kp1, des1 = orb.detectAndCompute(scanner_img, None)
        #     kp2, des2 = orb.detectAndCompute(db_img, None)
        #
        #     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        #     matches = bf.match(des1, des2)
        #     matches = sorted(matches, key=lambda x: x.distance)
        #     # print(len(matches))
        #     # print(matches)
        #     # img3 = cv2.drawMatches(scanner_img, kp1, db_img, kp2, matches, None,
        #     #                       flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        #     #
        #     # cv2.imshow("img3", img3)
        #     # cv2.waitKey(0)
        #     # cv2.destroyAllWindows()
        #     if len(matches) > 50:
        #         return True
        #     else:
        #         return False
