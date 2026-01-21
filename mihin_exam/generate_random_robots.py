import random
import math

rand_numbers = []

for i in range(50):
    rand_numbers.append(random.random())

lambda_input = 5
output_numbers = []

for i in range(len(rand_numbers)):
    output_numbers.append(-1 / lambda_input * math.log(rand_numbers[i], math.exp(1)))

for i in range(len(output_numbers)):
    print('Вычисленное число по формуле:', round(output_numbers[i], 2), '                Случайное число из нормального распределения, нужно для проверки и подстановки в формулу', round(rand_numbers[i], 2))