name = input("enter your name : ")

# len = length
# it tells you how many characters there are in your name (it includes spaces too)
# ex : slyzoo = 6 (characters)
result_1 = len(name)
print(f"the length of your name : {result_1}")

# the .find method finds a character
# .find finds the first occurance of the character, and tells you where it is (it starts at 0 not 1)
result_2 = name.find("o")
print(f"the first 'o' : {result_2}")

# the .rfind method finds a character but in reverse order
# .find finds the last occurance of the character, and tells you where it is 
result_3 = name.rfind("o")
print(f"the second 'o' : {result_3}")

# if the find / rfind cant find the character then it will return -1

# .capitalize capitalizes the first letter, and lowers the rest
name_1 = name.capitalize() # dont forget to add the parentheses
print(f"your name capitalized (first letter capped) : {name_1}")

# .upper captitalizes the whole string
name_2 = name.upper()
print(f"the whole name capped : {name_2}")

# .lower lowercases every letter
name_3 = name.lower()
print(f"your whole name lowercased : {name_3}")

# the .isdigit returns true or false if the str has digits in it or not
name_4 = name.isdigit()
print(f"is digit? : {name_4}")

# the .isalpha returns true or false if the str has alphabetical letters in it or not
name_5 = name.isalpha()
print(f"is alphabetical? : {name_5}")

# .count counts how many of a character there is
name_6 = name.count("o")
print(f"there are {name_6} o's in your name")

# .replace replaces any character with either another character or nothing
# another character ex :
name_7 = name.replace("o", "0")
print(f"your new name : {name_7}")
# empter character ex :
name_7 = name.replace("o", "")
print(f"your new name : {name_7}")

# to get more info on str methods
print(help(str))
