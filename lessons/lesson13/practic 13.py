import os


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)

def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line

for data_line in read_file():
    with open (new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)
        new_file.write(data_line)

homework_path = os.path.dirname(base_path)
lessons_file_path = os.path.join(homework_path, 'lesson13', 'data2.txt')
print(lessons_file_path)

with open(lessons_file_path) as lesson_file:
    print(lesson_file.read())
