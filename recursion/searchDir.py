from os import listdir, path


def searchDir(fName, dir="./"):
    for file in listdir(dir):
        if file == fName:
            print("{} found in {}".format(fName, dir))
            return  # return to find more matches
        elif os.path.isdir(file):  # if its a directory
            searchDir(fName, dir+file)  # search that directory

fName = input("Enter the filename of the file you want to find: ")
dir = input("Enter the directory you want to search (blank for current): ")

searchDir(fName, dir if dir != "")
