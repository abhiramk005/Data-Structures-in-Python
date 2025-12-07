#In selection sort find the minimum value in the array and then
#add it to the front(i)
#These shift operations are time consuming so we can also use swap

def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range (i+1,n):
            if arr[j]<arr[min]:
                min=j
        min_value=arr.pop(min)
        arr.insert(i,min_value)
    print("sorted array: ",arr)

array=[64,34,25,12,22,11,90,5]
selectionSort(array)