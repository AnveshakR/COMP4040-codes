import random
from time import time, time_ns

def countingSort(A):
    k = 0
    size = len(A)

    for i in range(size): # finds the largest number in the array
        if A[i] > k:
            k = A[i]

    count = [0] * (k + 1) # creates an array of size k, i.e. the largest number

    for i in A: # iterates over the loop and counts the number of times each number has appeared, and increments the corresponding indice
        count[i] += 1

    i = 0
    for j in reversed(range(k + 1)): # iterates over the loop in a reverse order to make it stable
        for a in range(count[j]):
            A[i] = j
            i += 1

    return A

# bucket sort with input numbers between 0 and 1

def insertionSort(A):
    for i in range(1, len(A)):
        up = A[i]
        j = i - 1
        while j >= 0 and A[j] > up: 
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = up     
    return A     
              
def bucketSort(A, slot_num=10): # slot_num slots, each slot's size is 1/slot_num
    
    bucket = []
    for i in range(slot_num):
        bucket.append([]) # create slot_num buckets: [[], [], ..., []]
    
    # Put array elements in different buckets 
    for x in A:
        bucket_indx = int(slot_num * x) # locate its bucket
        bucket[bucket_indx].append(x)
      
    # Sort individual buckets 
    #print("Distribution of numbers in buckets")
    for i in range(slot_num):
        bucket[i] = insertionSort(bucket[i])
        #print(bucket[i])
    
    bucket_size = [len(bucket[i]) for i in range(slot_num)]
    
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])): # note that range(0) contains nothing
            A[k] = bucket[i][j]
            k += 1
    return A

# Bucket sort for an input array with numbers greater than 1

def bucketSort1(A, NumOfBuckets=10):
    max_A = max(A)
    min_A = min(A)
  
    # range (for buckets)
    range_A = (max_A - min_A) / NumOfBuckets
  
    bucket = []
  
    # create empty buckets
    for i in range(NumOfBuckets):
        bucket.append([])
  
    # scatter the array elements into the correct bucket
    for i in range(len(A)):
        diff = (A[i] - min_A) / range_A - int((A[i] - min_A) / range_A)
  
        # append the boundary elements to the lower array
        if (diff == 0 and A[i] != min_A): # boundary
            bucket[int((A[i] - min_A) / range_A) - 1].append(A[i])
        else:
            bucket[int((A[i] - min_A) / range_A)].append(A[i])
    
    #print("Distribution of numbers in buckets")
    #for i in range(NumOfBuckets):
    #    print(bucket[i])
  
    # Sort each bucket individually
    for i in range(len(bucket)):
        if len(bucket[i]) != 0:
            bucket[i].sort()
            # Gather sorted elements 
    
    bucket_size = [len(bucket[i]) for i in range(NumOfBuckets)]
    
    # to the original array
    k = 0
    for list in bucket:
        if list:
            for x in list:
                A[k] = x
                k += 1

    return A, bucket_size

def countingdriver(): # driver for countingsort()

    A = [2, 1, 3, 4, 0, 5, 3, 2, 7, 1, 0, 5, 6, 4, 2]
    print("Counting Sort in descending order")
    print("Original Array: ", A)
    print("Sorted Array: ",countingSort(A))

def bucketdriver(): # driver for bucketsort functions

    A = [round(random.uniform(0,50),2) for _ in range(100)] # generates random array of 100 numbers between 1 and 100
    bucketsort_timer, bucketsort1_timer = 0,0 # initialise time counters

    for i in range(100): # runs bucketsort functions 100 times

        # for bucketsort()
        start = time_ns()
        bucketSort([round(x/(max(A)+1), 2) for x in A]) # dividing every number by the max number + 1 and passing to function
        bucketsort_timer += time_ns() - start # adding bucketsort() running time to counter

        # for bucketsort1()
        start1 = time_ns()
        bucketSort1(A)
        bucketsort1_timer += time_ns() - start1 # adding bucketsort1() running time to counter

    print("Total running time(ns) for bucketsort(): ",bucketsort_timer)
    print("Total running time(ns) for bucketsort1(): ", bucketsort1_timer)

countingdriver()
print("\n")
bucketdriver()