import os

#file detection

path = "C:\\Users\\gavin\\OneDrive\\Desktop\\banana.txt"

if os.path.exists(path):
    print("that location exists")

    if os.path.isfile(path):
        print("that is a file")

    elif os.path.isdir(path):
        print("that is a directory")
        
else:
    print("that doest exist")













































