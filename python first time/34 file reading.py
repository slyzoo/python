try:
    #always use \\ when using file paths
    with open("C:\\Users\\gavin\\OneDrive\\Desktop\\banana.txt") as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print("file not found")














































