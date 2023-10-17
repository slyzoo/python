#dictionary = a changeable unordered collection of unique key:value pairs fast because they use hashing allow us to access a value quickly


capitals = {"USA":"washington DC",
            "india":"new dehli",
            "china":"beijing",
            "russia":"moscow"}


capitals.update({"germany":"berlin"})

capitals.update({"USA":"las vegas"})

capitals.pop("china")

capitals.clear()

#print(capitals["russia"])

print(capitals.keys())

print(capitals.values())

print(capitals.items())

print(capitals.get("germany"))




for key,value in capitals.items():
    print(key,value)








