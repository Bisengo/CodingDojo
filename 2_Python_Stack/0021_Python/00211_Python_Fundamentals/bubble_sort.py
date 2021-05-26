def bubbleSort(arr):
    print(arr)
    n = len(arr)
    # traversing all elements of the array
    for j in range(n-1):
        print("\n\n","_"*50, "Iteration", j)
        #Last j+1 elements are already in correct position      
        for i in range(n-1-j):
            print("\n","*"*25, "\ncomparing", arr[i],arr[i+1])
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                print("swapped", arr[i],arr[i+1])
                print("array is now: ", arr)
            else:
                print("no need to swap", arr[i],arr[i+1])

arr = [14,46,43,27,57,41,45,21,70]
bubbleSort(arr)
print(arr)