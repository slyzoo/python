# validate username input exercise : 
#  1. username is no longer than 12 characters
#  2. username cannot contain any spaces
#  3. username cannot contain any digits

username = input("enter a username : ")

if len(username) > 12:
    print("your username cant be more than 12 characters")

elif not username.find(" ") == -1:
    print("your username cant contain spaces")

elif not username.isalpha():
    print("your username cant contain numbers")

else:
    print("welcome :3")
