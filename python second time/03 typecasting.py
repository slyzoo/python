# typecasting, the process of converting one datatype to another datatype
# i.e. strings, integer, float, boolean
# Explict and implicit

name = "slyzoo"
age = 16
gpa = 2.7
student = True


empty_string = (" ")# to space things out when executing the program

#this is explict (you have to change the datatype)


#prints the type of var it is, in this case name is a str
print("string :")
print(type(name))
print(name)

print(empty_string)

#prints the type of var it is, in this case name is a int
print("int :")
print(type(age))
print(age)

print(empty_string)

#prints the type of var it is, in this case name is a float
print("float :")
print(type(gpa))
print(gpa)

print(empty_string)

#prints the type of var it is, in this case name is a boolean
print("boolean :")
print(type(student))
print(student)

print(empty_string)

#prints the type of var it is, in this case it starts out as a boolean, then it changes into a float
age = float(age)
print(type(age))
print(age)

print(empty_string)

#prints the type of var it is, in this case it starts out as a float, then it changes into a int
gpa = int(gpa)
print(type(gpa))
print(gpa)

print(empty_string)

#prints the type of var it is, in this case it starts out as a boolean, then it changes into a str
student = str(student)
print(type(student))
print(student)

print(empty_string)

#prints the type of var it is, in this case it starts out as a int, then it changes into a boolean
#if you change a number to a boolean it will always be  true unless it is 0
age = bool(age)
print(age)

print(empty_string)

#prints the type of var it is, in this case it starts out as a str, then it changes into a boolean
#if you change a string to a boolean it will always be  true unless it is empty
name = bool(name)
print(name)

print(empty_string)

#implicit (when a value or var is converted to a diff datatype automatically)

# the datatype changes when preforming certain operations like divsion(/) 
x = 2
y = 2.0

x = x / y

print(type(x))
print(x)
