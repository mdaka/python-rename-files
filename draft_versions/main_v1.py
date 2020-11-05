# Read all image files with different sizes
# Convert each image by its size concatenating to file name + index + extension (all provided upon script), for example size 16x16 with "test" file name + png => 1_test_16x16.png
# (depends on file extension use different logic for the new generated file name, for example for svg file => 1_svg_test.svg)

# What needs for development
    # 1. list of files/folders from a path
    # 2. loop over each file
    # 3. get file data
    # 4. send file data to a method to generate for us a new file name ( also filter files by the extension type when neeeded)
    # 5. get new generated name and convert the core name to the new one

import os

folderPath = r"C:\Users\mdaka\Downloads\icons"
allFiles = os.listdir(folderPath)

for singleFile in allFiles:
    print(singleFile)