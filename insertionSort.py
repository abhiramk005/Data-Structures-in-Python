def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        insert_ind=i
        current_val=arr.pop(i)
        for j in range(i-1,-1,-1):
            if arr[j]>current_val:
                insert_ind=j
        arr.insert(insert_ind,current_val)
    print("sorted array: ",arr)

array=[64,34,25,12,22,11,90,5]
insertionSort(array)