# string indexing : accessing elements of a sequence using [] (the indexing operator)
# [start : end : step]
# start is inclusive, end is exclusive 


credit_card_number = "1234-1234-5678-55678"

# goal = 1

# prints the first character, in this case 1
# if you say [0] the computer will assume you want the start
print(credit_card_number[0])


# goal = 1-4

# prints the first 4 characters 
print(credit_card_number[0:4])
# you can also do this, python thinks its the same thing
print(credit_card_number[:4])


# goal = the second pair of 1-4

print(credit_card_number[5:9])

# goal 5-the end

print(credit_card_number[5:])


# goal the last number

# if you need the last (few) characters in an index use negative index
print(credit_card_number[-1])

# to get a step you need to use [::] to get to the step part
# step [2] prints every other digit (every second digit)
print(credit_card_number[::2])

# step [3] prints every third digit
print(credit_card_number[::3])

