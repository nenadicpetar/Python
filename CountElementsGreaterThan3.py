# ===============
# Opcija 1
# ===============

my_list = [-1, 1, -2, 3, -4, 4, 6, 5, 7]
count = 0

for elem in my_list:
    if elem > 3:
        count += 1
        
print(count)


# ===============
# Opcija 2
# ===============

my_list = [-1, 1, -2, 3, -4, 4, 6, 5, 7]

count = sum(1 for elem in my_list if elem > 3)

print(count)