import os

folderPath = r'C:\Users\mdaka\Downloads\icons\1_logs'
allFilesOrFolders = os.scandir(folderPath)

for fileOrFolder in allFilesOrFolders:
    # print(fileOrFolder)
    path = os.path.join(folderPath, fileOrFolder)
    if os.path.isfile(path):
        print(os.stat(path))
        print(fileOrFolder.name)