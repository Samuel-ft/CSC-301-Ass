def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print("Bubble Sort:", bubble_sort([5,8,16,10,3,1,4]))


#Complexity
#•	Best: O(n) (optimized version)
#•	Average: O(n²)
#•	Worst: O(n²)
