

# the program gets the operator and the numbers
operator = input("wut operator do you need? (+, -, *, /) : ")
num1 = float(input("wut number is it? (1) : "))
num2 = float(input("wut number is it? (2) : "))

# if the operator is + it adds the nums up for the result and prints the result
if operator == "+" : 
    result = num1 + num2

    #rounds to 3 decimal places
    print(round(result, 3))

# if the operator is - it subtracts the nums for the result and prints the result
elif operator == "-" : 
    result = num1 - num2
    print(round(result, 3))

# if the operator is * it multiplys the nums for the result and prints the result
elif operator == "*" : 
    result = num1 * num2
    print(round(result, 3))

# if the operator is / it divides the nums for the result and prints the result
elif operator == "/" : 
    result = num1 / num2
    print(round(result, 3))

else:
     print(f"{operator} is not a valid operator")

    

