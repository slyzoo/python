#exception = events detected during execution that interupt the flow of the program


try:
   numerator = int(input("enter a number to divide: "))
   denominator = int(input("entera number to divide by: "))
   result = numerator / denominator

except ZeroDivisionError as e :
   print(e)
   print("bruh you cant do that, do another number")

except ValueError as e :
   print(e)
   print("enter only numbers idiot")

except Exception as e :
   print(e)
   print("something went wrong, congrats to you for doing that")

else:
   print(result)
   
finally:
   print("this will always execute")






































