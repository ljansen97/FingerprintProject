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
output = dir + "converted" + "\\"

# Create the converted directory
if not os.path.isdir(output):
    print("Generating output dir...")
    os.mkdir(output)

for file in files:
    # Create input path
    file_in = dir + file
    
    # Open the image file
    img = cv2.imread(file_in)
    
    #resize file
    img = cv2.resize(img, (64, 96))
    
    # Replace PNG with BMP
    output_file = output + file
    output_file = output_file.replace("png", "bmp")
    output_file = output_file.replace("\\", "/")
    print(output_file)
    cv2.imwrite(output_file, img)
    
    # Counter + 1 for progress bar
    count += 1
    
    # Print the progress bar
    pb.print_progress_bar(count)
    
print("Successfully converted %s files" % str(number_of_files))
