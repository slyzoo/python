import os

path_1 = "C:\\Users\\gavin\\OneDrive\\Desktop\\banana.txt"
path_2 = "C:\\Users\\gavin\\OneDrive\\Desktop\\banana(banana).txt"
try:
    os.remove(path_1)
    os.remove(path_2)
    #os.rmdir(path) to remove folders / directories

except FileNotFoundError:
    print("that file is not found")

except PermissionError:
    print("you do not have perms to delete that")

except OSError:
    print("you cannot delete that using that function")

else:
    print(path_1+"was deleted")
    print(path_2+"was deleted")














































