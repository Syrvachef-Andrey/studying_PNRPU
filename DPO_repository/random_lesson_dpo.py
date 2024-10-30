# 1 таск

# import random as rn
#
# rand_list = [rn.randint(-1000, 1000) for i in range(rn.randint(1, 100))]
#
# print(rand_list)
# rand_list = rand_list[::-1]
# print(rand_list)

# 2 таск

# import random as rn
#
# first_rand_list = [rn.randint(-1000, 1000) for i in range(rn.randint(1, 100))]
# second_rand_list = [rn.randint(-1000, 1000) for i in range(len(first_rand_list))]
# third_rand_list = []
# for i in range(len(first_rand_list)):
#     if i % 2 == 0:
#         third_rand_list.append(first_rand_list[i])
#     else:
#         third_rand_list.append(second_rand_list[i])
#
# print(third_rand_list)

# 3 таск

# import random as rn
#
#
# def rand_int(a, b):
#     return [rn.randint(a, b) for i in range(rn.randint(1, 30))]
#
#
# def rand_float(a, b):
#     return [rn.uniform(a, b) for i in range(rn.randint(1, 30))]
#
#
# def rand_str(a, b):
#     return [chr(rn.randint(a, b)) for i in range(rn.randint(1, 30))]
#
#
# int_list = rand_int(0, rn.randint(1, 100))
# float_list = rand_float(0, rn.uniform(5, 20))
# str_list = rand_str(40, rn.randint(41, 100))
# sum_list = list(set(int_list + str_list + float_list))
# print(sum_list)

# 4 таск

import random as rn


# def dict_random(length):
#     return {f'key_{i}': rn.choice([rn.randint(-20, 20), rn.uniform(1, 10)]) for i in range(length)}
#
#
# dict_task = dict_random(rn.randint(1, 15))
# print(dict_task)
#
# unic_dict = {}
# for key, value in dict_task.items():
#     if value not in unic_dict:
#         unic_dict[value] = []
#     unic_dict[value].append(key)
#
# list_of_result = [(value, keys) for value, keys in unic_dict.items()]
# print(list_of_result)
# print(len(dict_task), len(list_of_result))

# 5 таск

import random as rn


def dict_random(length):
    return {f'key_{i}': rn.choice([rn.randint(-20, 20), rn.uniform(1, 10)]) for i in range(length)}


first_dict_task = dict_random(rn.randint(10, 20))
second_dict_task = dict_random(len(first_dict_task))
print(second_dict_task)
print(first_dict_task)

inter_dict = set(first_dict_task.values()).intersection(set(second_dict_task.values()))

dict_of_result = {k: v for k, v in {**first_dict_task, **second_dict_task}.items() if v in inter_dict}
print(dict_of_result)
print(len(first_dict_task), len(second_dict_task), len(dict_of_result))