import cv2 as cv2
import random
import numpy
import os
import copy
import sys

dir = sys.argv[1]

if(not os.path.isdir(os.path.join(dir, "cropped"))):
    os.mkdir(os.path.join(dir, "cropped"))

def opdelen(filename, output_folder):
    print(output_folder)
    image = cv2.imread(filename)
    image_copy = copy.copy(image)

    divisions_size = 200
    divisions_offset = 60
    divisions_horizontal = (image.shape[1] / divisions_size)
    divisions_vertical = (image.shape[0] / divisions_size)

    parts = []

    for x in range(0, int(divisions_horizontal)):
        for y in range(0, int(divisions_vertical)):
            x1 = ((x*divisions_size)-divisions_offset)
            if(x1 < 0): x1 = 0
            y1 = ((y*divisions_size)-divisions_offset)
            if(y1 < 0): y1 = 0
            x2 = ((x*divisions_size)+divisions_size)
            if(x2 > image.shape[1]): x2 = image.shape[1]
            if(x1 != 0): x2 -= divisions_offset
            y2 = ((y*divisions_size)+divisions_size)
            if(y2 > image.shape[0]): y2 = image.shape[0]
            if(y1 != 0): y2 -= divisions_offset
            parts.append(((x1, y1),(x2,y2)))

    currentColor = 1
    currentCrop = 0
    print(output_folder)
    output_folder_image = os.path.join(output_folder + "\\", os.path.splitext(filename)[0])
    print(output_folder_image)
    #os.mkdir(output_folder_image)

    for part in parts:
        cropped = image[part[0][1]:part[1][1], part[0][0]:part[1][0]]
        #cv2.imwrite(os.path.join(output_folder_image, "cropped_" + str(currentCrop) + ".bmp"), cropped)
        cv2.rectangle(image_copy, part[0], part[1], currentColor == 1 and (random.randint(100,255),random.randint(100,255),random.randint(100,255)) or (random.randint(100,255),random.randint(100,255),random.randint(100,255)), 2)
        currentCrop += 1
        currentColor *= -1

    #cv2.imshow("Output", image_copy)


#opdelen("vinger.bmp", "F:\\ProjectRedHat\\FingerprintProject\\Stitching\\Opdeler\\output")
files = [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]
for file in files:
    #print(os.path.join(dir, "cropped"))
    opdelen(os.path.join(dir, file), os.path.join(dir, "cropped\\"))
#cv2.waitKey(0)
#cv2.destroyAllWindows()