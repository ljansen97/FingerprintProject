from Algorithm import Algorithm
import numpy as np
import cv2

class TM_COEFF_NORMED_Algorithm(Algorithm):
    def __init__(self, treshold):
        self.treshold = treshold

    def image_resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation=inter)

        # return the resized image
        return resized

    def test(self, scanner_img, db_img):
        print("Scanner: " + scanner_img)
        print("DB: " + db_img)
        scanner_img = cv2.imread(scanner_img, cv2.IMREAD_GRAYSCALE)
        db_img = cv2.imread(db_img, cv2.IMREAD_GRAYSCALE)
        # scanner_w, scanner_h = scanner_img.shape[::-1]
        db_w, db_h = db_img.shape[::-1]
        scanner_img = self.image_resize(scanner_img, width=db_w)

        cv2.imshow("Scanner", scanner_img)
        cv2.imshow("DB", db_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        result = cv2.matchTemplate(db_img, scanner_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.2)#self.treshold)
        unpacked = zip(*loc[::-1])
        print(list(unpacked))
        for pt in unpacked:
            print(pt)

        return True