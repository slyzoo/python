
#str.format = optional method that gives users more control when displaying output







animal = "cow" 
item ="moon"

print("the "+ animal + " jumped over the " + item)

print("the {} jumped over the {}".format(animal,item))

print("the {} jumped over the {}".format("cow","moon")) #keyword argument

print("the {} jumped over the {}".format(item,animal)) #keyword argument

print("the {0} jumped over the {1}".format(animal,item)) #positional agrument

print("the {1} jumped over the {1}".format(animal,item))  #positional agrument

print("the {0} jumped over the {0}".format(animal,item))  #positional agrument

print("the {1} jumped over the {0}".format(animal,item))  #positional agrument

print("the {animal} jumped over the {item}".format(animal = "cow" ,item = "moon"))

text ="the {} jumped over the {}"

print(text.format(animal, item))



name = "slyzoo"


print ("hello my name is {:10} nice to meet you".format(name))

print ("hello my name is {:<10} nice to meet you".format(name))

print ("hello my name is {:>10} nice to meet you".format(name))

print ("hello my name is {:^10} nice to meet you".format(name))




number = 1000   #3.14

print("the number pi is {:.3f}".format(number))
print("the number pi is {:,}".format(number))
print("the number pi is {:b}".format(number))
print("the number pi is {:o}".format(number))
print("the number pi is {:X}".format(number))
print("the number pi is {:x}".format(number))
print("the number pi is {:x}".format(number))
print("the number pi is {:e}".format(number))
print("the number pi is {:E}".format(number))