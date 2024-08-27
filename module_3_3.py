def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params(11)
print_params(12, "asd")
print_params(12, "asd", False)
print_params()
values_list = [1, "asdas", True]
values_dict = {1: "aaa", "sss": 'False', True: '333'}
print_params(*values_list)
print_params(*values_dict)
values_list2 = [1, "asdasd"]
print_params(*values_list2, 42)