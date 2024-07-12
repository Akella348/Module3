def print_params(a, b, c):
    print(a, b, c)
#print_params(b = 25)  убрал в коммент чтобы код выполнялся
#print_params(c = [1, 2, 3])  убрал в коммент чтобы код выполнялся
values_list = [1, True, 'Denis']
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 1]
print_params(*values_list_2, 42)