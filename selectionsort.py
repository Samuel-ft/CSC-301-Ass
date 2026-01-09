def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print("Selection Sort:", selection_sort([5,8,16,10,3,1,4]))


#Complexity
#•	Best: O(n²)
#•	Average: O(n²)
#•	Worst: O(n²)
