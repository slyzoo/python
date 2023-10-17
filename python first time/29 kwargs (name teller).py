


#**kwargs = parameter that will pack all arguments into a dictionary, useful so that a function can accept a varying amount of keyword arguments


#the ** is importiant not really anything else
def hello(**names):
    #print("hello "+ kwargs['first'] + " " + kwargs['last'])
    print('hello',end=" ")
    for key,value in names.items():
        print(value,end=" ")


hello(title ="ms.",first="slyzoo", last = "himes")
























