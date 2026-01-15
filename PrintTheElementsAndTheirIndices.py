# ===========
# Opcija 1
# ===========

my_list = [3, 4, 5, 6]

if len(my_list) == 0:
    print("Prazna lista")
else:
    for i in range(len(my_list)):
        print(my_list[i], i)
        
        
# ===========
# Opcija 2
# ===========

my_list = [3, 4, 5, 6]

if not my_list:
    print("Prazna lista")
else:
    for i, elem in enumerate(my_list):
        print(elem, i)
