import sys
import os
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
    img = Image.open(file_in)
    
    # Replace PNG with BMP
    file = file.replace(".png", ".bmp")
    
    # Create output path
    file_out = output + file
    
    # Save the file
    img.save(file_out)
    
    # Counter + 1 for progress bar
    count += 1
    
    # Print the progress bar
    pb.print_progress_bar(count)
    
print("Successfully converted %s files" % str(number_of_files))
