a = [5, 8, 10, 45, 67, 22, 30]

def mergeSort(a): # driver function

    width = 1 # assuming size of smallest array as 1
    n = len(a)
    while (width < n):
        l=0 # starting from left of array
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1) # consideration for non 2-power sized input         
            merge(a, l, m, r)
            l += width*2
        width *= 2 # increasing sub array size by powers of 2
    return a
    
def merge(a, l, m, r): # main merge function
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
  
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
  
  
print("Unsorted: ", a)
  
print("Sorted: ", mergeSort(a))