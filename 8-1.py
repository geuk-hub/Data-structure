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