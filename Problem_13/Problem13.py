import numpy as np

file = open('data','r')
x = (file.read().split())
y = list(map(int, x))
x = np.array(y)
print(x.sum())


