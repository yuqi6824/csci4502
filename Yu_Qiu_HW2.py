__author__ = 'qiuyu'

import sys, getopt, math

def task_1():
    opts, args = getopt.getopt(sys.argv[1:], "n:",["f1=", "a1="])
    for op, value in opts:
        if op == "--f1":
            '''csvF1 = file(value, 'rb')
            reader = csv.reader(csvF1)'''
            f = open(value, "r")
            data = []
            for line in f:
                row = [x for x in line.split(",")]
                if len(row) > 0:
                    data.append(row)
            for i in range(0, len(data)):
                correct_data = data[i][5].replace("\r\n", "")
                data[i][5] = correct_data
        elif op == "--a1":
            col = []
            for j in range(0, 6):
                if value == data[0][j]:
                    for i in range(1, len(data)):
                        col.append(data[i][j])
        elif op == "-n":
            min_max = []
            if value == "min_max":
                max = col[0]
                min = col[0]
                #find max
                for x in col:
                    if max < x:
                        max = x
                #find min
                for y in col:
                    if min > y:
                        min = y
                for x in col:
                    y = ((float(x) - float(min))/(float(max) - float(min))) * (1 - 0) + 0
                    print x, y
            elif value == "z_score":
                total = 0
                z_score = []
                for x in col:
                    total = total + float(x)
                #average
                avg = total/len(col)
                #standard deviation
                square_total = 0
                for x in col:
                    square_total = square_total + (float(x) - avg) * (float(x) - avg)
                    stan_de = math.sqrt(square_total/len(col))
                    z = (float(x) - float(avg)) / stan_de
                    print x, z
    f.close()

def task_2():
    opts, args = getopt.getopt(sys.argv[1:], "",["f1=", "a1=", "f2=", "a2="])
    data = []
    data_2 = []
    col = []
    col_2 = []
    new_col = []
    new_col_2 = []
    for op, value in opts:
        if op == "--f1":
            f = open(value, "r")
            #data = []
            for line in f:
                row = [x for x in line.split(",")]
                if len(row) > 0:
                    data.append(row)
            for i in range(0, len(data)):
                correct_data = data[i][5].replace("\r\n", "")
                data[i][5] = correct_data
        elif op == "--a1":
            for j in range(0, 6):
                if value == data[0][j]:
                    for i in range(1, len(data)):
                        col.append(data[i][j])
        elif op == "--f2":
            f = open(value, "r")
            #data_2 = []
            for line in f:
                row = [x for x in line.split(",")]
                if len(row) > 0:
                    data_2.append(row)
            for i in range(0, len(data_2)):
                correct_data_2 = data_2[i][5].replace("\r\n", "")
                data_2[i][5] = correct_data_2
        elif op == "--a2":
            for j in range(0, 6):
                if value == data_2[0][j]:
                    for i in range(1, len(data_2)):
                        col_2.append(data_2[i][j])
        #correlation analysis
    if len(col) <= len(col_2):
        for i in range(0, len(col)):
            new_col_2.append(col_2[i])
        #calculate ai*bi
        ab = 0
        for j in range(0, len(col)):
            ab = ab + float(col[j]) * float(new_col_2[j])
        #calculat avg of a and b
        total_a = 0
        for x in col:
            total_a = total_a + float(x)
        avg_a = total_a/len(col)
        total_b = 0
        for y in new_col_2:
            total_b = total_b + float(y)
        avg_b = total_b/len(new_col_2)
        #standard deviation of A and B
        square_total_a = 0
        for i in range(0, len(col)):
            square_total_a = square_total_a + (float(col[i]) - avg_a) * (float(col[i]) - avg_a)
        stan_de_a = math.sqrt(square_total_a/len(col))
        square_total_b = 0
        for i in range(0, len(new_col_2)):
            square_total_b = square_total_b + (float(new_col_2[i]) - avg_b) * (float(new_col_2[i]) - avg_b)
        stan_de_b = math.sqrt(square_total_b/len(new_col_2))
        print (ab - len(col) * avg_a * avg_b) / (len(col) * stan_de_a * stan_de_b)

    else:
        for i in range(0, len(col_2)):
            new_col.append(col[i])
    #calculate ai*bi
        ab = 0
        for j in range(0, len(col_2)):
            ab = ab + float(col_2[j]) * float(new_col[j])
        #calculat avg of a and b
        total_a = 0
        for x in new_col:
            total_a = total_a + float(x)
        avg_a = total_a/len(new_col)
        total_b = 0
        for y in col_2:
            total_b = total_b + float(y)
        avg_b = total_b/len(col_2)
        #standard deviation of A and B
        square_total_a = 0
        for i in range(0, len(new_col)):
            square_total_a = square_total_a + (float(new_col[i]) - avg_a) * (float(new_col[i]) - avg_a)
        stan_de_a = math.sqrt(square_total_a/len(new_col))
        square_total_b = 0
        for i in range(0, len(col_2)):
            square_total_b = square_total_b + (float(col_2[i]) - avg_b) * (float(col_2[i]) - avg_b)
        stan_de_b = math.sqrt(square_total_b/len(col_2))
        print (ab - len(col_2) * avg_a * avg_b) / (len(col_2) * stan_de_a * stan_de_b)

if __name__ == '__main__':
    #task_1()
    task_2()