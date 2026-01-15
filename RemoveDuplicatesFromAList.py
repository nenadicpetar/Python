# ===========
# Opcija 1
# ===========

my_list = [1, 1, 2, 3, 4, 4, 6]
no_duplicates = list(set(my_list))

print(no_duplicates)


# ===========
# Opcija 2
# ===========

my_list = [1, 1, 2, 3, 4, 4, 6]
no_duplicates = list(dict.fromkeys(my_list))
print(no_duplicates)

dict.fromkeys(my_list)
{1: None, 2: None, 3: None, 4: None}