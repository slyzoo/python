import os

source = "banana(banana).txt"
destination = "C:\\Users\\gavin\\OneDrive\\Desktop\\banana(banana).txt"

try:
    if os.path.exists(destination):
        print("there is a file there already")
    else:
        os.replace(source,destination)
        print(source+"was moved")
except FileNotFoundError:
    print(source + " file not found")










































