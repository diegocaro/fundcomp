def insertionsort(A):
    N = len(A)
    for i in range(1, N):
        k = A[i]
        j = i-1
        while j >= 0 and A[j] > k:
            A[j+1] = A[j]
            A[j] = k
            j = j - 1
            
a = [9,5,1]
insertionsort(a)