my_int = 7
my_float = 4.8
my_str = "Всем привет"
my_list = ['a', '3']
my_tuple = ('b', '4')
my_dict = {'город': 'Петропавловск-Камчатский', 'страна': 'Россия'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')