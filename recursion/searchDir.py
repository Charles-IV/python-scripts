from os import listdir, path
from colorama import init, Fore, Style

# init colorama
init()


def searchDir(fName, dir, found):
    for file in listdir(dir):

        if file == fName:
            found.append(path.join(dir, file))
            print(Fore.GREEN+"{} - found".format(path.join(dir, file)))
            #return  # return to find more matches
            # don't return - keep searching in directory for more
        elif path.isdir(path.join(dir, file)):  # if its a directory
            #print("{} is a directory, entering".format(file))
            searchDir(fName, path.join(dir, file), found)  # search that directory
        else:
            print(Fore.RED+"{}".format(path.join(dir, file)))
    return found  # return list of files


def searchDir2(fName, dir, dummy=[]):  # alternative method friend showed me
    found = []
    for file in listdir(dir):
        #print(Fore.RED+"looking at {} in {}".format(file, dir), end="")
        if file == fName:
            found.append(path.join(dir, file))
            #print(Fore.GREEN+"\r{}".format(found))
            #return  # return to find more matches
            # don't return - keep searching in directory for more
        elif path.isdir(path.join(dir, file)):  # if its a directory
            #print("{} is a directory, entering".format(file))
            for foundFile in searchDir2(fName, path.join(dir, file), found):  # search that directory
                found.append(foundFile)
    return found

fName = input("Enter the filename of the file you want to find: ")
dir = input("Enter the directory you want to search (blank for current): ")

print(Style.RESET_ALL + "\n\n", searchDir(fName, "./" if dir == "" else dir, []))
