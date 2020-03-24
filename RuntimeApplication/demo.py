import os, sys, pyfprint
import cv2, numpy

images = [f for f in os.listdir(".") if f.startswith("scan") and f.endswith("pgm")]
count = len(images) + 1

# capture single image, with option of writing to file
def img_show(args):
    try: height, width, img = pyfprint.capture_img()
    except Exception as e:
        print("image capture failed:", str(e))
        return

    if len(img):
        img = numpy.array(img, numpy.uint8).reshape(height,width)
        cv2.imshow("Scan", img)
        print("< Press 's' to save image and close or any other key to close without saving")
        key = chr(cv2.waitKey(0))

        try:
            if key == "s":
                global count
                file = f"scan{count}.pgm"
                cv2.imwrite(file, img)
                count += 1

                images.append(file)
                print(f"image saved to {file}")
        except: pass
        cv2.destroyAllWindows()

# capture a number of images, amount to capture can be specified as argument
def img_sample(args):
    try: n = max(int(args[0]), 0)
    except: n = 5
    print(f"Getting ready to take a sample of {n} images")

    imgs = []
    for i in range(n):
        print(f"Capturing image {i+1}/{n}...")
        try:
            height, width, img = pyfprint.capture_img()
            imgs.append(numpy.array(img, numpy.uint8).reshape(height, width))
        except: break

    display = numpy.concatenate(imgs, axis=0)
    cv2.imshow("result", display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

commands = {
    "scan": img_show,
    "c": img_show, # just a 'scan' shortcut
    "sample": img_sample,
}

if __name__ == '__main__':
    print("Initializing...")
    print(f"< Found {len(images)} images in current directory:")
    print("  ", " ".join(images))

    print("< Opening fingerprint device...")
    try: pyfprint.open_device("message")
    except Exception as e:
        print("Error! Failed to open device:", str(e))
        sys.exit(-1)

    print("< Device ready, type 'scan' to capture an image or 'sample {n=5}' to capture n images at once")
    while True:
        try: arg = input("> ")
        except KeyboardInterrupt: arg = "q"
        if arg == "q": break

        arg = arg.split(" ")
        if len(arg):
            cb = commands.get(arg[0])
            if cb: cb(arg[1:])

    print("< Terminating...")
    print("< Closing fingerprint device...")
    pyfprint.close_device()