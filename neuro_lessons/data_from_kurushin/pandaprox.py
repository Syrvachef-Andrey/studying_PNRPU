import numpy as np
import pandas as pd

boats = pd.ExcelFile("data.xlsx")
boat_prices = boats.parse('Лист1')

D = boat_prices.values[:,0:9].astype(np.double)
Y = boat_prices.values[:,9:10].astype(np.double).flatten()

print(np.isnan(D).any(), np.isinf(D).any())
print(np.isnan(Y).any(), np.isinf(Y).any())

for i in range(len(D)):
    if np.isnan(D[i]).any():
        print(i)

for i in range(len(D[0])):
    a, b = np.polyfit(
        np.sort(D[:,i]),
        np.linspace(0,1,len(D[:,i])),1
    )
    D[:,i] = D[:,i] * a + b

X = D.sum(axis=1)

a, b = np.polyfit(X, Y, 1)

for x, y in zip(X, Y):
	print(y, x*a + b)