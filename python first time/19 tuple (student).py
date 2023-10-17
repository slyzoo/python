#tuple = collection is ordered and unchangeable used to group together related data



student = ("slyzoo","16","male")


print(student.count("slyzoo"))
print(student.count("16"))
print(student.count("male"))


print(student.index("male"))
print(student.index("16"))
print(student.index("slyzoo"))

for x in student:
    print(x)

if "slyzoo" in student:
    print("slyzoo is here:")