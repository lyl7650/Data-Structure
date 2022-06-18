# coding = utf-8


import numpy as np

def select_sort(li):
    """选择排序"""
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        li[min_idx], li[i] = li[i], li[min_idx]
    return li
            
if __name__ == "__main__":
    li = np.random.randint(0, 100, size = 10)
    print(li)
    print(select_sort(li))
    #print(li)