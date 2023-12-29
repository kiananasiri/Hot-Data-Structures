def merge_sort( array , low , high):
    mid = (low + high) // 2
    if low >= high:
        return
    merge_sort(array , low , mid)
    merge_sort(array , mid+1 , high)
    
    p1 = low
    p2 = mid+1
    b = []
    while p1 <= mid or p2 <= high:
        if p1 > mid:
            b.append(array[p2])
            p2+=1
        elif p2 > high:
            b.append(array[p1])
            p1 += 1
        elif array[p1] <= array[p2]:
            b.append(array[p1])
            p1+=1
        else:
            b.append(array[p2])
            p2+=1
    array[low : high+1 ]= b 
    
if __name__ == "__main__":
    a=[4,5,3,2,6,7,1,8]
    merge_sort(a , 0 , len(a)-1)
    print(a)
    
    
    
    