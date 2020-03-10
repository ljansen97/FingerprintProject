import sys
import os
import cv2
from PIL import Image
from console_progressbar import ProgressBar

# The directory is the 1st argument
dir = sys.argv[1]

# Put the files in a list
files = [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]

# Count the number of files
number_of_files = len(files)

# Initialize a progress bar
pb = ProgressBar(total=number_of_files, prefix='Converting', suffix='Converted', decimals=2, length=50, fill='#', zfill='.')

# Initialize the counter
count = 0

# Fix the argument
dir = dir.replace("/", "\\")
if dir[-1] != "\\":
    dir += "\\"

# Print the message
print("Converting dir: %s" % dir)

# Output dir
output = dir + "converted deel 2" + "\\"

# Create the converted directory
if not os.path.isdir(output):
    print("Generating output dir...")
    os.mkdir(output)

for file in files:
    # Create input path
    file_in = dir + file
    
    # Open the image file
    img = cv2.imread(file_in)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,31,2)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    img = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    
    # Resize file
    height = img.shape[0]
    width = img.shape[1]
    division = int(height / 64)
    cropped = []
    cropcounter = 0
    
    for i in range(0, division - 1):
        cropped.append(img[(i * 64):(i * 64) + 64, 0:width])
    
    for image in cropped:
        
        file = file.replace(".png", "")
        output_file = file + "_" + "cropped" + str(cropcounter) + ".bmp"
        cv2.imwrite(os.path.join(output, output_file), image)
        cropcounter += 1
    
    # Counter + 1 for progress bar
    count += 1
    
    # Print the progress bar
    pb.print_progress_bar(count)
    
print("Successfully converted %s files" % str(number_of_files))
