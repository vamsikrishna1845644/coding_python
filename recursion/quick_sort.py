def quicksort(arr,low , high):
     
    if (low < high ):
        partition_index = f(arr,low,high)
        quicksort(arr, low ,partition_index-1)
        quicksort(arr, partition_index+1 ,high)

def f(arr, low ,high):
    pivot = arr[low]
    i = low
    j = high
    while(i < j):
        while( arr[i]<=pivot and i<=high):
            i+=1
        while( arr[j]>pivot and j >=low):
            j-=1
        if(i < j):
            #swap the elements
            arr[i],arr[j] = arr[j] , arr[i]
    arr[low],arr[j] = arr[j] , arr[low]
    return j

arr = [7,4,3,2,9,12,6,5,89,100]
quicksort(arr, 0,len(arr)-1)
print(arr)
        
