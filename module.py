import os
import shutil

src=input("Enter the source path\t")
dest=input("Enter the destination path\t")

src=src+'/'
dest=dest+'/'
listOfFiles=os.listdir(src)
print(listOfFiles)

for file in listOfFiles:
    shutil.copy((src+file),dest)

