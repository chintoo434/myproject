import time
tm=time.time()

def heapify(arr, n, i):
        large=i
        l=2*i+1
        r=2*i+2

        if(l<n and arr[i]<arr[l]):
            large=l
        if(r<n and arr[large]<arr[r]):
            large=r
        if(large!=i):
            arr[i], arr[large]=arr[large], arr[i]
            heapify(arr, n, large)

def heapsort(arr, n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i]=arr[i], arr[0]
        heapify(arr, i, 0)

arr = [ 12, 11, 13, 5, 6, 7]
heapsort(arr,len(arr))
for i in range(0, len(arr)):
    print(arr[i])
