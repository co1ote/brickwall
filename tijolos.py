import os
import sys
import json

def possuiTijolo(nums, limit):
    sum = 0
    for num in nums:
        sum += num
        if sum == limit:
            return 0
        elif sum > limit:
            return 1

def cortes(arr, pos):
    h = 0
    for x in arr:
        y = possuiTijolo(x, pos)
        h += y
    #print(f'#{pos}: {h}')
    return h

def tijolos(arr):
    min_cortes = 10001
    cortes_possiveis = sum(arr[0])

    for x in range(1, cortes_possiveis):
        c = cortes(arr, x)
        if (c < min_cortes):
            min_cortes = c

    return min_cortes

if __name__ == '__main__':
    with open('array.json') as json_file:
        data = json.load(json_file)

        result = tijolos(data)

        print(result)
