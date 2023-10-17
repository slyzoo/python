#scope = the region that a variable is recognized. a variable is only available from the inside the region it was created.
#a global and locally scoped versions of a var can be created


name = "slyzoo"  #global


def display_name():
    name = "himes" #local
    print(name)


def display_name():
    print(name)



display_name()
print(name)


#how python finds vars
#local 
#enclosing
#global
#built in




