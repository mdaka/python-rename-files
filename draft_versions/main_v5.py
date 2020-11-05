import os
from PIL import Image

allowedImageTypes = ['.png', '.jpg']

folderPath = r'C:\Users\mdaka\Downloads\icons\1_logs'
allFilesOrFolders = os.scandir(folderPath)

for fileOrFolder in allFilesOrFolders:
    # print(fileOrFolder)
    path = os.path.join(folderPath, fileOrFolder)
    if os.path.isfile(path):
        fileName = fileOrFolder.name
        extension = os.path.splitext(fileName)[1]
        if extension in allowedImageTypes:
            print(fileName)
            im = Image.open(path)
            newFileName = '1_' + str(im.width) + 'x' + str(im.height) + extension
            print(newFileName)
            print("-------------------")
            # print(os.stat(path))