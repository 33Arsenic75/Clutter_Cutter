import os
import shutil

path = input("Enter the path of the directory:")
#Ex: /Users/hg/Desktop also create the directory Unsorted in the src directory.
n = int(input("Enter the no. of letters for sorted folder names:")
#Ex: 2 => then if I have file "welcome.txt" then folder name will be "we"

def func2():
    srcpath = f"{path}/Unsorted"
    srcfiles = os.listdir(srcpath)

    destpath = f"{path}/Sorted"

    destdirs = list(set([filename[0:n] for filename in srcfiles]))

    def create(dirname, destpath):
        full_path = os.path.join(destpath, dirname)
        try:
            os.makedirs(full_path)
        except FileExistsError:
            pass
        return full_path

    def move(filename, dirpath):
        shutil.move(os.path.join(srcpath, filename),dirpath)

    targets = [(folder, create(folder, destpath)) for folder in destdirs]

    for dirname, full_path in targets:
        for filename in srcfiles:
            if dirname == filename[0:n]:
                move(filename, full_path) 
while True:
    if len(os.listdir("/Users/hg/Desktop/Unsorted")) != 0:
        func2()
