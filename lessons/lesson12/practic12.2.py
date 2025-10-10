import json

class CountryData:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()
        self.country = self.data['Country']
        self.avg_temp = self.data['avg_temp']
        self.comfort = self.is_comfort()

    def read_file(self):
        file_data = open(self.filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def is_comfort(self):
        return self.avg_temp > 25

    def __str__(self):
        return f'File {self.filename}, with data: {self.data}'
    def __repr__(self):
        return f'File {self.filename}, with data: {self.data}'
    def __lt__(self, obj):
        return self.avg_temp < obj.avg_temp
    def __le__(self, obj):
        return self.avg_temp <= obj.avg_temp
    def __add__(self, obj):
        return self.avg_temp + obj.avg_temp



class CountryData3(CountryData):
    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']



data1 = CountryData('data1.txt')
print(data1.data)
print(data1.country)
print(data1.avg_temp)
data2 = CountryData('data2.txt')
print(data2.data)
print(data2.country)
print(data2.avg_temp)
print(data1.comfort)
data3 = CountryData3('data3.txt')
print(data3.avg_temp)
print(data3.min_temp)
print(data1 < data2)
print(data1 <= data2)
print(data1 > data2)
print(data1 >= data2)
print(data1 + data2)
print(data1)