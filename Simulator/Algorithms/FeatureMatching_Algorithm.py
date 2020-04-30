from Algorithm import Algorithm
import cv2
import os


class FeatureMatching_Algorithm(Algorithm):
    def test(self, scanner_img, db_img, settings):
        parsed_settings = self.parseSettings(settings=settings)

        if 'min_count_for_match' not in parsed_settings.keys():
            min_count_for_match = 200
        else:
            min_count_for_match = parsed_settings["min_count_for_match"]

        bs = scanner_img
        bd = db_img
        scanner_img = cv2.imread(scanner_img, cv2.IMREAD_GRAYSCALE)
        db_img = cv2.imread(db_img, cv2.IMREAD_GRAYSCALE)

        # Initiate ORB detector
        sift = cv2.xfeatures2d.SIFT_create()
        # find the keypoints and descriptors with ORB
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
        if count > int(min_count_for_match):
            return True
        else:
            return False
