def SortByCounting(A):
    temp = [()] * len(A)
    for i in range(len(A)):
        k = 0
        for num2 in A:
            if A[i] > num2:
                k += 1
        temp[k] = temp[k][:] + (A[i],)
    B = []
    for item in temp:
        if len(item) > 0:
            for number in item:
                B.append(number)
    return B


def SortByInclusion(A):
    B = [A[0], ]
    for element in A[1:]:
        i = 0
        while len(B) > i and B[i] <= element:
            i += 1
        B.insert(i, element)
    return B


def SortByExtraction(A):
    for i in range(len(A)):
        el = min(A[i:])
        del A[A[i:].index(el) + i]
        A.insert(i, el)
    return A


def SortByExchange(A):
    for i in range(len(A)):
        isChange = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                isChange = True
        if not isChange:
            return A
    return A


import time
import timeit


file = open("Random Numbers", "r")
text = file.read().split()
num = []
for element in text:
    num.append(int(element))
file.close()
n = [100, 500, 1000, 2500, 5000, 7500, 10000, 20000, 30000]
for count in n:
    Sample = num[:count]
    print("SortByCounting", count, min(timeit.Timer(lambda: SortByCounting(Sample)).repeat(repeat=20, number=1)))
    Sample = num[:count]
    print("SortByInclusion", count, min(timeit.Timer(lambda: SortByInclusion(Sample)).repeat(repeat=20, number=1)))
    Sample = num[:count]
    print("SortByExtraction", count, min(timeit.Timer(lambda: SortByExtraction(Sample)).repeat(repeat=20, number=1)))
    Sample = num[:count]
    print("SortByExchange", count, min(timeit.Timer(lambda: SortByExchange(Sample)).repeat(repeat=20, number=1)))




a = '''
n = [100, 500, 1000]
for count in n:
    Sample = num[:count]
    fullTime = []
    for i in range(11):
        start_time = time.time_ns()
        A = SortByCounting(Sample)
        end_time = time.time_ns()
        if i != 0:
            fullTime.append(end_time - start_time)
    print("SortByCounting", count, (max(fullTime) + min(fullTime)) / 2, (max(fullTime) + min(fullTime)) / 2 / 1000000000)
    Sample = num[:count]
    fullTime = []
    for i in range(11):
        start_time = time.time_ns()
        A = SortByInclusion(Sample)
        end_time = time.time_ns()
        if i != 0:
            fullTime.append(end_time - start_time)
    print("SortByInclusion", count, (max(fullTime) + min(fullTime)) / 2, (max(fullTime) + min(fullTime)) / 2 / 1000000000)
    Sample = num[:count]
    fullTime = []
    for i in range(11):
        start_time = time.time_ns()
        A = SortByExtraction(Sample)
        end_time = time.time_ns()
        if i != 0:
            fullTime.append(end_time - start_time)
    print("SortByExtraction", count, (max(fullTime) + min(fullTime)) / 2, (max(fullTime) + min(fullTime)) / 2 / 1000000000)
    Sample = num[:count]
    fullTime = []
    for i in range(11):
        start_time = time.time_ns()
        A = SortByExchange(Sample)
        end_time = time.time_ns()
        if i != 0:
            fullTime.append(end_time - start_time)
    print("SortByExchange", count, (max(fullTime) + min(fullTime)) / 2, (max(fullTime) + min(fullTime)) / 2 / 1000000000)'''