import os

folderPath = r'C:\Users\mdaka\Downloads\icons\1_logs'
# List all files in a directory using os.listdir
allFilesOrFolders = os.listdir(folderPath)

for fileOrFolder in allFilesOrFolders:
    # print(fileOrFolder)
    if os.path.isfile(os.path.join(folderPath, fileOrFolder)):
        print(fileOrFolder.name)