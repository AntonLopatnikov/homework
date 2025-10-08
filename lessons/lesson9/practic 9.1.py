

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

new_list = filter(is_even, my_list)
print(list(new_list))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = filter(lambda x: x % 2 ==0, my_list)
print(list(new_list))


