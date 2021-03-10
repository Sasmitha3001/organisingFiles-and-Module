import os
import shutil

path1=input("Enter the name of the directory that needs to be sorted\t")
listOfFiles=os.listdir(path1)
print(listOfFiles)

for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if(ext==''):
        continue

    if(os.path.exists(path1+'/'+ext)):
        shutil.move(path1+'/'+file,path1+'/'+ext+'/'+file)
    else:
        os.makedirs(path1+'/'+ext)
        shutil.move(path1+'/'+file,path1+'/'+ext+'/'+file)

