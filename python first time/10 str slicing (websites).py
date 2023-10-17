#slicing = create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]   (start, stop)
#for slices there are positive indentation and negitive indentation, negitive goes backwards from positive

name = "slyzoo"

#you can leave the first number empty ONLY if you are ok with it being 0
first_name = name[0:3]

#you can leave the last number empty on the second digit if you want the rest of the str
last_name = name[3:6]

#for step you can leave the first two slots empty but you HAVE to have the colons 

#if you use 1 as your step it will provide the enitre string (str)

#if you use two as the step it will show every second character from the string (str)
funky_name = name[0:6:2]

#to use negitive numbers for step the first two slots have to be empty
reversed_name = name[::-1]

website1 ="https://www.firefox.com/"
website2 = "https://www.wikipedia.org/"

slice = slice(12,-5)


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#slices are weird broo
print(website1[slice])
print(website2[slice])
