my_list = [5, 7, 3, 12, 7, 2, 3, 15, 2, 13, 5]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)