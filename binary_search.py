def binarySerach(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=right+left//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1

array=[1,3,5,7,9,11,13,15,17,19]
target=15

result=binarySerach(array,target)
print(result if result!=-1 else "Not found")


