


import math
import numpy as np
import collections


def find_factors(n):
    numList = list(range(1,math.ceil(n/2)+1))
    count = 0
    finalList = []
    for x in numList:
        if(n%x == 0):
            finalList = finalList + [x]
        count = count+1
    return sum(finalList)



def get_all_totals(n):
    finalList = []
    for x in range(1,n+1):
        finalList = finalList + [find_factors(x)]
    return finalList


k = get_all_totals(10000)
print(k)

final_num = 0
count = 1
for x in k:
    if(x<len(k)-1):
        print('d('+str(count)+') = '+ str(x) +' ?? ' + 'd('+ str(x)+') = ' + str(k[x-1]))
        if(count == k[x-1] and x != count):
            final_num = final_num+count+x
            print(x)
            print(count)
    count+=1


print(final_num/2)






