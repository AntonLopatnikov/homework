import json
def read_file(filename):
    file_data = open(filename, 'r')
    #data= file_data.read()
    data = json.load(file_data)
    file_data.close()
    return data
data1 = read_file('data1.txt')
data2 = read_file('data2.txt')

print(data1['Country'])
print(data1['avg_temp'])
print(data2['Country'])
print(data2['avg_temp'])
print(data1)
print(data2)

