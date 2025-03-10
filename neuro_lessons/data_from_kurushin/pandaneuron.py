import numpy as np
import pandas as pd

boats = pd.ExcelFile("data.xlsx")
boat_prices = boats.parse('Лист1')

D = boat_prices.values[:,0:9].astype(np.double)
Y = boat_prices.values[:,9:10].astype(np.double).flatten()

for i in range(len(D[0])):
    a, b = np.polyfit(
        np.sort(D[:,i]),
        np.linspace(0,1,len(D[:,i])),1
    )
    D[:,i] = D[:,i] * a + b

w = np.zeros((len(D[0]))).astype(np.double)

α =  0.2 
β = -0.4 
σ = lambda x: x

def f(x):
    s = β + np.sum(x @ w)
    return σ(s)

def train():
    global w
    _w = w.copy()
    for x, y in zip(D, Y):
        w += α * (y - f(x)) * x
    return (w != _w).any()

n = 0            
while train() and n < 10:
    print(w)
    n += 1

for x, y in zip(D, Y):
    print(x, y, round(f(x)))
