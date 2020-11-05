import os

allowedImageTypes = ['.png', '.jpg']

folderPath = r'C:\Users\mdaka\Downloads\icons\1_logs'
allFilesOrFolders = os.scandir(folderPath)

for fileOrFolder in allFilesOrFolders:
    # print(fileOrFolder)
    path = os.path.join(folderPath, fileOrFolder)
    if os.path.isfile(path):
        fileName = fileOrFolder.name
        if os.path.splitext(fileName)[1] in allowedImageTypes:
            print(fileName)
            # print(os.stat(path))