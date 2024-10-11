classes = [input() for i in range(int(input()))]
list_of_numbers = '0123456789'
list_of_letters = 'АБВГДЕЖЗИЙКЛМНОП'
for clas in classes:
    if len(clas) == 2 and clas[0] in list_of_numbers and clas[1].isdigit() == 1:
        if clas[1] in list_of_letters and clas[0] in list_of_numbers:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')