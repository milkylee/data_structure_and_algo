def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)

#1.) Rename the function as optimized_bubble_sort
#2.) Introduce a 'swapped' variable before the inner loop to track any swaps made during each iteration of the outer loop.
#3.) Set 'swapped' to 'True' inside the inner loop whenever a swap is performed.
#4.) After each iteration of the inner loop, check the value of 'swapped'. If it remains 'False', it signifies that no swaps were made, indicating that the list is already sorted and the algorithm can terminate early.