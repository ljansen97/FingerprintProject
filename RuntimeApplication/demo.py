import sys, pyfprint
import cv2, numpy

def save_test_img():
    """
        Example code that reads fingerprint and loads the result into opencv
    """
    try: pyfprint.open_device()
    except Exception as e:
        print("Failed to open device:", str(e))
        sys.exit(-1)

    count = 0
    while True:
        try: arg = input("> ")
        except KeyboardInterrupt: arg = "q"

        if arg == "q": break

        try: height, width, img = pyfprint.capture_img()
        except Exception as e:
            print("image capture failed:", str(e))
            continue

        if len(img):
            img = numpy.array(img, numpy.uint8).reshape(height, width)
            if arg == "show":
                cv2.imshow("result", img)
                cv2.waitKey(0)
            else:
                print("image saved")
                cv2.imwrite(f"test_{count}.pgm", img)
            count += 1

    pyfprint.close_device()

if __name__ == '__main__':
    save_test_img()