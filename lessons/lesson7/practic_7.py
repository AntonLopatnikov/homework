i = 0

while i < 5:
    print("hello")
    i+= 1


while True:
   user_input = input(' Enter something: ')
   if user_input =='exit':
       break
   elif user_input == 'skip':
       continue
   elif len(user_input) > 10:
       print('your input is too long')
   else:
       print('input is ok')
print('Goodbye')


a = 1
b = 5
c = 4
d = 7
y = 0
main_number = 47

def calculate(numb):
    if y == 0:
        print(numb)
    else:
        print(numb + main_number)

calculate(a)
calculate(b)
calculate(c)
calculate(d)



a = 1
b = 5
c = 4
d = 7
y = 0
main_number = 47

def calculate(numb):
    if y == 0:
        return numb
    else:
        return numb + main_number

calculate(a)
calculate(b)
calculate(c)
calculate(d)
fdsfds