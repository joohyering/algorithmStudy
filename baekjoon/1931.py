#greedy
#입력 수정할 것 (시간초과)

import math

#회의 개수
N = int(input())

#data
#numpy배열 사용하면 훨씬 더 간단하게 구현 가능
data = []
dataX = []
dataY = []
for i in range(N) :
    data += [list(map(int, input().split()))]
for i in range(N) :
    dataX += [data[i][0]]
    dataY += [data[i][1]]

result = 0
checkList = list(range(N))
tempMin = math.pow(2,31)


while checkList != [] :
    for i in checkList :
        if dataY[i] < tempMin :
            tempMin = dataY[i]
    checkList.clear()
    for j in range(N) :
        if dataX[j] >= tempMin :
            checkList += [j]
    print(checkList)
    print(tempMin)
    tempMin = math.pow(2, 31)
    result += 1

print(result)
