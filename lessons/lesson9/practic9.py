my_list = [1,2,3,4,5]

def mul_by2(x):
    return x * 2

new_list = map(mul_by2, my_list)
print(list(new_list))

new_list = map(lambda x: x * 2, my_list)
print(list(new_list))

new_list = map(lambda x: x * 5 if x < 10 else x * 2, my_list)
print(list(new_list))