#set = collection which is unorderd, unindexed. no dublicate values


silverware ={"fork","spoon","knife"}

dishes ={'bowl', 'plate', "cup","knife"}

dinner_table = silverware.union(dishes)

silverware.add("salad fork")
silverware.remove("salad fork")
silverware.clear
silverware.update(dishes)
dishes.update(silverware)


for y in silverware:
    print(y)

for x in dinner_table:
    print(x)

print(silverware.difference(dishes))


print(silverware.intersection(dishes))




