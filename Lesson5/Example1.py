my_list = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_list.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_list.close()
my_list = open('test.txt', 'r')
content = my_list.readlines()
print(content)
my_list.close()
