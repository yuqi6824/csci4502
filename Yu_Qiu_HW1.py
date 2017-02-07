__author__ = 'qiuyu'

import sys,math

f = open("magic04.data.txt", "r")
data = []
for line in f:
    row = [x for x in line.split(",")]
    if len(row) > 0:
        data.append(row)
#N
N = len(data)
i = 0
j = int(sys.argv[1]) - 1
min = data[0][j]
max = data[0][j]
total = 0
order = []
for i in range(0, N):
    #min
    '''if data[i][j] < min:
        min = data[i][j]'''

    #max
    '''if data[i][j] > max:
        max = data[i][j]'''

    #total
    total = total + float(data[i][j])

    #order first step
    order.append(data[i][j])

#order second step
count = len(order)
for i in range(1, count):
    key = float(order[i])
    k = i - 1
    while k >= 0:
        if float(order[k]) > key:
            order[k + 1] = order[k]
            order[k] = key
        k -= 1

#min
min = order[0]

#max
max = order[N-1]

#mean
mean = total/len(data)

#standard deviation
square_total = 0
for i in range(0, N):
    square_total = square_total + (float(data[i][j]) - mean) * (float(data[i][j]) - mean)
stan_de = math.sqrt(square_total/N)

#Q1
Q1 = (float(order[4755]) + float(order[4756]))/2

#median
median = (float(order[9510]) + float(order[9511]))/2

#Q3
Q3 = (float(order[14265]) + float(order[14266]))/2

#IQR
IQR = Q3 - Q1

print N, min, max, "%.4f"%mean, "%.4f"%stan_de, "%.4f"%Q1, "%.4f"%median, "%.4f"%Q3, "%.4f"%IQR
f.close()