my_file = open('file_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()

my_file = "file_2.txt"

with open(my_file, 'r') as file:
    lines = [line for line in file.readlines() if line != '\n']

    print(f"В файле непустых строк:", len(lines))

    for line, words_cnt in {l: len(l.split()) for l in lines}.items():
        print(f'Строка {line[:50]}... содержит {words_cnt} слова')