import numpy as np
import math
n = 6

total = []





for x in range(1,(n**2)+1):
    print(x)

    a = "{0:b}".format(x)

    b = list(a)

    results = list(map(int, b))



    while(len(results)<n):
        results.append(0)

    results2 = np.array(results)
    check = sum(results2==0)
    print(check)
    if(check == int(n/2)):
        total.append(results)

print(total)


