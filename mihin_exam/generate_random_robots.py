import random
import math

rand_numbers = []

for i in range(50):
    rand_numbers.append(random.random())

lambda_input = 10
output_numbers = []

for i in range(len(rand_numbers)):
    output_numbers.append(-1 / lambda_input * math.log(rand_numbers[i], math.exp(1)))

for i in range(len(output_numbers)):
    print(output_numbers[i], rand_numbers[i])