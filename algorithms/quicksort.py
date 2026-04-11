import math
import random

def pickPivot(arr, left, right, strategy = "deterministic"):
    if strategy == "deterministic":
        pi = math.floor((left + right)/2-1)
        
    elif strategy == "randomised":
        pi = random.randint(len(arr))
    
    elif strategy == "medianPick":
        rand_indizes = []
        for i in range(3):
            rand_indizes.append(random.randint(0,len(arr)))
        a,b,c = rand_indizes[0],rand_indizes[1],rand_indizes[2]
        if a>c:
            rand_indizes[0],rand_indizes[2] = rand_indizes[2],rand_indizes[0]
        if b>c:
            rand_indizes[1],rand_indizes[2] = rand_indizes[2],rand_indizes[1]
        if a>b:
            rand_indizes[0],rand_indizes[1] = rand_indizes[1],rand_indizes[0]
        pi = rand_indizes[1]

    return pi
  
def quicksort(A, left, right):
    if right-left <= 1: # Recursion Basis
        return
     # Dividing ---------------------------------------------------------------
    pi = pickPivot(A, left, right) # pivot index
    p = A[pi] # pivot element
    L = left
    R = right-1 # Left and Right borders of the search interval
    while R>=L:
        # Finding the left and right swap indizes 
        j=L
        while j<=R: 
            if A[j]>=p:
                LL = j
                break
            j+=1
        j=R
        while j>=L:
            if A[j]<=p:
                RR=j
                break
            j-=1
                  
        # Swapping 
        A[RR], A[LL] = A[LL], A[RR]
        if pi == LL:
            pi = RR
        elif pi == RR:
            pi = LL
        #Updating the borders of the searching interval
        if LL<pi<RR:
            L = LL + 1
            R = RR - 1
        elif LL==pi<RR:
            L = LL 
            R = RR - 1
        elif LL<pi==RR:
            L = LL + 1
            R = RR
        else:
            break
            

# Recursion----------------------------------------------------------
    if left - pi < right - pi: # smaller first
        left1 = left 
        right1 = pi
        left2 = pi + 1
        right2 = right
    else:
        left1 = pi +1 
        right1=right
        left2 = left 
        right2 = pi
    quicksort(A, left1, right1)
    quicksort(A, left2, right2)     
