import numpy as np

import time


for x in range(2300,19400):
    n = np.array(np.arange(1, x + 1))

    q = n.sum()
    if(q%510510 == 0):
        k = np.array(np.arange(1,int(q/2)+1))

        output = np.equal(np.mod(q,k),0).sum() +1


        print(str(x)+" : " +str(output))

        if (output > 500):
            print("here")
            print(q)
            break













