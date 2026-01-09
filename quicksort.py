def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print("Quick Sort:", quick_sort([5,8,16,10,3,1,4]))

#Complexity
#Case	Complexity
#Best	O(n log n)
#Average	O(n log n)
#Worst	O(n²) (bad pivot)
#Space	O(log n) recursive
