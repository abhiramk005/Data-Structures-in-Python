def partition(arr,low,high):
    pivort=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivort:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quickSort(arr,low=0,high=None):
    if high is None:
        high=len(arr)-1

    if low<high:
        pivort_index=partition(arr,low,high)
        quickSort(arr,low,pivort_index-1)
        quickSort(arr,pivort_index+1,high)

array=[64,34,25,12,22,11,90,5]
quickSort(array)
print(array)