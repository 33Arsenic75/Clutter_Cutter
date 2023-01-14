import os
import shutil




def func2():
    srcpath = "/Users/hg/Desktop/Unsorted"
    srcfiles = os.listdir(srcpath)

    destpath = "/Users/hg/Desktop/Sorted"

    # extract the ten letters from filenames and filter out duplicates
    destdirs = list(set([filename[0:2] for filename in srcfiles]))

    def create(dirname, destpath):
        full_path = os.path.join(destpath, dirname)
        try:
            os.makedirs(full_path)
        except FileExistsError:
            pass
        return full_path

    def move(filename, dirpath):
        shutil.move(os.path.join(srcpath, filename),dirpath)
    # create destination directories and store their names along with full paths
    targets = [(folder, create(folder, destpath)) for folder in destdirs]

    for dirname, full_path in targets:
        for filename in srcfiles:
            if dirname == filename[0:2]:
                move(filename, full_path) 
while True:
    if len(os.listdir("/Users/hg/Desktop/Unsorted")) != 0:
        func2()