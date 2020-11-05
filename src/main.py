#!/usr/bin/python

# Helper resources => {
#   https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html
#   https://pythonexamples.org/python-pillow-get-image-size/
#   https://realpython.com/working-with-files-in-python/#getting-file-attributes

#   destDirectory = os.path.join(folderPath, destDirectory) # instead of folderPath + '\\' +  destDirectory
# }

# Example of running this script => python main_v6.py abc 12 "C:\coding\python_icon_script"
# Usage Example => python main_v6.py 1_logout 1_logout "C:\Users\mdaka\Downloads\icons\2 - Copy"


import os
import sys
import shutil

from PIL import Image

#print('Argument List:', str(sys.argv))
if len(sys.argv) < 3:
    raise ValueError('Please provide the following args in this order [ prefixName, newFolderName, pathToSrcFolder] to create a new destination folder with new renamed files...')

#folderPath = r'C:\Users\mdaka\Downloads\icons\1_logs'
prefixName = sys.argv[1]
newFolderName = sys.argv[2]

if len(sys.argv) > 3:
    folderPath = sys.argv[3]
else:
    folderPath = os.getcwd() # We can use os.getcwdb() or os.path.dirname(os.path.abspath(__file__))


# print(os.stat(srcPath))


def createDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:
        print("Directory has not beed created because its already existed: ", dirName)
    return dirName

def getAllowedImageTypes():
    return ['.png', '.jpg', 'jpeg']

def getNewImageName(path, prefixName, extension):
    im = Image.open(path)
    newFileName = prefixName + '_' + str(im.width) + 'x' + str(im.height) + extension
    return newFileName

def getFileName(path, prefixName, extension):
    fileType = (extension[1:]).lower() # remove the first dot from the string 
    
    if extension in ['.txt', '.pdf']:
        newFileName = prefixName + extension
    else:    
        newFileName = prefixName + '_' + fileType + extension
    
    return newFileName

def copyFile(srcFile, destDirectory, newFileName):
    dest = os.path.join(destDirectory, newFileName) # Instead of destDirectory + '\\' + newFilename
    shutil.copy(srcFile, dest, follow_symlinks=False)
    print(newFileName)
    print("-------------------")

def main():
    destFolderPath = os.path.join(folderPath, newFolderName)

    # os.path.join(os.getcwd() , newFolderName) # this will get the path where the script file is running
    destDirectory = createDirectory(destFolderPath) # destDirectory = createDirectory('C:\\Users\\mdaka\\Downloads\\icons\\2 - Copy\\test\\')
    
    allowedImageTypes = getAllowedImageTypes()
    for fileOrFolder in os.scandir(folderPath):
        
        srcPath = os.path.join(folderPath, fileOrFolder)

        if os.path.isfile(srcPath):
            fileName = fileOrFolder.name
            extension = (os.path.splitext(fileName)[1]).lower()
            fileName = os.path.splitext(fileName)[0]

            if extension in allowedImageTypes:
                newFileName = getNewImageName(srcPath,prefixName,extension)
                copyFile(srcPath, destDirectory, newFileName)
                
            elif extension in ['.psd', '.eps', '.svg']:
                newFileName = getFileName(srcPath,prefixName,extension)
                copyFile(srcPath, destDirectory, newFileName)

            elif extension in ['.txt', '.pdf']:
                tempFileName = prefixName + '_' + fileName
                newFileName = getFileName(srcPath,tempFileName ,extension)
                copyFile(srcPath, destDirectory, newFileName)



if __name__ == '__main__':
    main()