def apply_all_func(int_list, *functions):
    info = {}
    for func in functions:
        info[func.__name__] = func(int_list)
    return info


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
