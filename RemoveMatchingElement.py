my_list = [3, 3, 2, 1]
elem_to_remove = 3

if not my_list:
    print("Prazna lista")
elif my_list.count(elem_to_remove) == 0:
    print("Nije pronađeno")
else:
    for i in range(my_list.count(elem_to_remove)):
        my_list.remove(elem_to_remove)
        
print(my_list)