import random

array = [random.randint(-10, 16) for i in range(11)]
print(array)



# Insertion sort
def insertion_sort(array: list[int]) -> list[int]:
    
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            
            else:
                break
    return array
            
        
print(insertion_sort(array))


# Selection sort
def selection_sort(array: list[int]) -> list[int]:
    
    for i in range(len(array) - 1):
        m = array[i]
        p = i
        for j in range(i+1, len(array)):
            if m > array[j]:  
                m = array[j]
                p = j
            
        if p != i:
            t = array[i]
            array[i] = array[p]
            array[p] = t
            
        
    return array

print(selection_sort(array))



# Merge

arr = [9,5,-3,4,7,8,-8]
def merge(a: list[int], b: list[int]) -> list[int]:
    N = len(a)
    M = len(b)
    c = []

    i = 0
    j = 0

    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c

def merge_sort(array: list[int]) -> list[int]:
    N1 = len(array) // 2
    a1 = array[:N1]
    a2 = array[N1:]
    
    if len(a1) > 1:
        a1 = merge_sort(a1)
        
    if len(a2) > 1:
        a2 = merge_sort(a2)
        
    return merge(a1, a2)


# print(merge(a = [1, 4, 10, 11], b = [2, 3, 3, 4, 8]))
print(merge_sort(arr))


# Quick sort
def quick_sort(a: list[int]) -> list[int]:
    if len(a) > 1:
        x = a[random.randint(0, len(a) -  1)]
        lower = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        higher = [u for u in a if u > x]
        a = quick_sort(lower) + eq + quick_sort(higher)
        
    return a

print(quick_sort(array))


# bubble sort
def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a)-1):
        for j in range(1, len(a) - 1 - i):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
     
    return a       
        
print(bubble_sort(array))