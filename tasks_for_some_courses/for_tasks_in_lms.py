import random
import sys


def table(qunt):
    if qunt == 2:
        print('x    y')
        for x in range(2):
            for y in range(2):
                print(x, y, sep='    ')
    elif qunt == 3:
        print('x    y    z')
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    print(x, y, z, sep='    ')
    else:
        print('x    y    z    v')
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    for v in range(2):
                        print(x, y, z, v, sep='    ')
    print("\n")


def list_of_true(quant, s):
    input_list = []
    if s == 'ручной':
        for i in range(quant ** 2):
            x = int(input())
            if x < 0 or x > 1:
                return None
            input_list.append(x)
    else:
        for i in range(quant ** 2):
            input_list.append(random.randint(0,1))
    return input_list


def final_table(quant, input_list):
    print("Финальная таблица")
    counter = 0
    list_of_table = []
    if quant == 2:
        print('x    y    F')
        for x in range(2):
            for y in range(2):
                list_of_string = []
                print(x, y, input_list[counter], sep='    ')
                if input_list[counter]:
                    list_of_string.append(x)
                    list_of_string.append(y)
                    list_of_string.append(input_list[counter])
                    list_of_table.append(list_of_string)
                counter += 1
    elif quant == 3:
        print('x    y    z    F')
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    list_of_string = []
                    print(x, y, z, input_list[counter], sep='    ')
                    if input_list[counter]:
                        list_of_string.append(x)
                        list_of_string.append(y)
                        list_of_string.append(z)
                        list_of_string.append(input_list[counter])
                        list_of_table.append(list_of_string)
                    counter += 1
    else:
        print('x    y    z    v    F')
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    for v in range(2):
                        list_of_string = []
                        print(x, y, z, v, input_list[counter], sep='    ')
                        counter += 1
                        if input_list[counter]:
                            list_of_string.append(x)
                            list_of_string.append(y)
                            list_of_string.append(z)
                            list_of_string.append(v)
                            list_of_string.append(input_list[counter])
                            list_of_table.append(list_of_string)
                        counter += 1
    return list_of_table



def sdnf(list_of_func, quant):
    print("СДНФ: ", end='')
    str_sdnf = ''
    if quant == 2:
        for ind_str in range(len(list_of_func)):
            for ind in range(len(list_of_func[ind_str]) - 1):
                if ind == 0:
                    if not(list_of_func[ind_str][ind]):
                        str_sdnf += '!x'
                    else:
                        str_sdnf += 'x'
                else:
                    if not(list_of_func[ind_str][ind]):
                        str_sdnf += '!y'
                    else:
                        str_sdnf += 'y'
            if ind_str + 1 != len(list_of_func):
                str_sdnf += ' V '
    print(str_sdnf, "\n")


def sknf(list_of_func, quant):
    print("СКНФ")

print("Введите кол-во переменных")
quantity_variable = int(input())
bulev_list = []
if 2 <= quantity_variable <= 4:
    table(quantity_variable)
    print('Выберите режим заполнения значений функции: "ручной" или "случайный"')
    s = str(input())
    if s == 'ручной':
        print("Введите значения когда булева функция истинна")
        bulev_list = list_of_true(quantity_variable, s)
        if bulev_list is None:
            print("Неправильно введен список значений функций")
            sys.exit()
    else:
        print("Случйно сгенерированнеые значения")
        bulev_list = list_of_true(quantity_variable, s)
    list_of_func = final_table(quantity_variable, bulev_list)
    sdnf(list_of_func, quantity_variable)
    sknf(list_of_func, quantity_variable)
else:
    print("Недопустимое кол-во переменных")
