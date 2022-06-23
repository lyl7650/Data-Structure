import numpy as np


def insert_sort(li):
    for i in range(1, len(li)):
        for j in range(i, 0, -1):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
    return li

li = np.random.randint(100,size=10)
print(li)
print(insert_sort(li))
