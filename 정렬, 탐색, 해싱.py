## 문제 1. 주어진 데이터에 대해서 버블 정렬, 선택 정렬, 삽입 정렬을 사용하여 출력한다. 정렬 방법을 이해하기 위해서 각 패스마다 배열에 저장된 데이터를 출력한다.
## 데이터는 다음을 사용한다. data = [24, 15, 29, 11, 47, 12]
## 실습 노트에 각 정렬 방법에 대해서 각 패스마다 정렬되는 과정을 연습한다.
## 버블 정렬, 선택 정렬, 삽입 정렬의 3개 정렬 방법의 실행 시간은 O(n2)이 되며 2개의 for 루프 사용하여 구현한다.
## 각 정렬 방법에 대해 같은 배열을 사용하기 위해서 정렬하기 전에 복사해서 사용한다. import copy / d = copy.deepcopy(data)

import copy

def printStep(arr, val) :
    print("Step%2d = " % val, end = '')
    print(arr)

def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        for j in range(i,0,-1) :
            if A[j] < A[j-1] :
                A[j], A[j-1] = A[j-1], A[j]
        printStep(A, n-i)

def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if A[j]< A[least] :
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1)

def insertion_sort(A) :
    n = len(A)
    for i in range(1,n) :
        key = A[i]
        j = i-1
        while j >=0 and A[j] > key :
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A, i)

data = [24, 15, 29, 11, 47, 12]
a = copy.deepcopy(data)
b = copy.deepcopy(data)
c = copy.deepcopy(data)

print("Before sorting")
print(data)
print("\nAfter bubble sorting")
bubble_sort(a)
print("\nBefore sorting")
print(data)
print("\nAfter selection sorting")
selection_sort(b)
print("\nBefore sorting")
print(data)
print("\nAfter insertion sorting")
insertion_sort(c)

## 문제 2. 난수 발생기를 사용하여 배열에 정수를 저장한다. 배열에 있는 정수를 버블 정렬, 선택 정렬, 삽입 정렬하여 각 정렬 방법마다 시간 측정을 하여 비교한다. 
## 또한 파이썬 리스트에서 제공하는 sort()를 사용하여 비교한다.

import random, copy, time

def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        for j in range(i,0,-1) :
            if A[j] < A[j-1] :
                A[j], A[j-1] = A[j-1], A[j]

def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if A[j]< A[least] :
                least = j
        A[i], A[least] = A[least], A[i]

def insertion_sort(A) :
    n = len(A)
    for i in range(1,n) :
        key = A[i]
        j = i-1
        while j >=0 and A[j] > key :
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

while(1) :
    n = int(input("Enter a number of data : "))
    if n == -1 :
        break
    data = []
    for i in range(n) :
        numbers = random.randint(0,n)
        data.append(numbers)
    d = copy.deepcopy(data)
    startTime = time.time()
    bubble_sort(d)
    endTime = time.time()
    print("Bubble sort elapsed time : %.3f seconds" %(endTime - startTime))
    startTime = time.time()
    selection_sort(d)
    endTime = time.time()
    print("Selection sort elapsed time : %.3f seconds" %(endTime - startTime))
    startTime = time.time()
    insertion_sort(d)
    endTime = time.time()
    print("Insertion sort elapsed time : %.3f seconds" %(endTime - startTime))
    startTime = time.time()
    d.sort()
    endTime = time.time()
    print("Python sort elapsed time : %.3f seconds\n" %(endTime - startTime))

## 문제 3. 난수 발생기를 사용하여 배열에 정수를 저장한다. 
## 배열을 deepcopy 하여 파이썬 리스트에서 제공하는 sort()를 사용하여 정렬한 후 
## 임의의 숫자에 대해서 정렬되지 않은 데이터에 대해서는 순차 탐색과 정렬된 데이터에 대해서는 이진 탐색하여 시간 측정을 비교한다. 
## 데이터를 찾으면 해당 인덱스를 출력한다.

import random, copy, time

def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        for j in range(i,0,-1) :
            if A[j] < A[j-1] :
                A[j], A[j-1] = A[j-1], A[j]

def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if A[j]< A[least] :
                least = j
        A[i], A[least] = A[least], A[i]

def insertion_sort(A) :
    n = len(A)
    for i in range(1,n) :
        key = A[i]
        j = i-1
        while j >=0 and A[j] > key :
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def sequential_search(A, key, low, high) :
    for i in range(low, high + 1) :
        if A[i].key == key :
            return i
        return None

def binary_search(A, key, low, high) :
    if (low <= high) :
        middle = (low + high) // 2
        if key == A[middle].key :
            return middle
        elif key < A[middle].key :
            return binary_search(A, key, low, middle - 1)
        else :
            return binary_search(A, key, middle + 1, high)
    return None

n = int(input("Enter a number of data : "))
data = []
for i in range(n) :
    numbers = random.randint(0,n)
    data.append(numbers)
d = copy.deepcopy(data)
startTime = time.time()
d.sort()
endTime = time.time()
print("Python sort elapsed time : %.3f seconds\n" %(endTime - startTime))

while(1) :
    search_number = int(input("Enter a number to search : "))
    if search_number == -1 :
        break
    if sequential_search(search_number) == None :
        print("%d is not in the list." %search_number)
    else :
        print("%d is in the list at index %d"%(search_number, ))
