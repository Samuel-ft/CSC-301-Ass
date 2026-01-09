def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

print("Insertion Sort:", insertion_sort([5,8,16,10,3,1,4]))



#Complexity
#•	Best: O(n) (nearly sorted list)
#•	Average: O(n²)
#•	Worst: O(n²)
