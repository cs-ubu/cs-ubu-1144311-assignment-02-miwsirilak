#!/usr/bin /env python3
from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    # YOUR CODE HERE
    import numpy as np
    a,b = np.array(A), np.array(b)
    n= len(A[0])
    x = np.array([0]*n)
    #1.elimination
    """n = len(A[0])
    print(f'n={n}')
    """
    for k in range(0,n-1): # pivot equation #k
        #print(f'เลือกสมการที่ {k}')
        for j in range(k+1, n): #eliminate eq #j
            if a[j,k] !=0.0:
            #print(f'\tกำจัดตัวแปรที่ {k},ออกจากสมการที่ {j}')
                lam = a[j][k]/a[k][k]
            #update A[j][k เป็นต้นไป]
                a[j,k:n] = a[j,k:n] - lam*a[k,k:n]
            #A[j][k+2] = A[j][k+2] - lam*A[k][k+2]
            #A[j][k+3] = A[j][k+3] - lam*A[k][k+3]
            #print(f'\t\tlambda={lam}')
            #update b[j]
                b[j] = b[j] - lam* b[k]

        """printm(A)
        print(b)
        """
    #2 back substitution
    for k in range(n-1, -1, -1): #2,1,0
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
        #print(f' k={k}')
        #A[k,0:n]*x[k:] = b[k:]
    #x = []
    return x.flatten()
print( solve (A,b))

"""print('==== A ====')
printm(A)
print('====b ====')
printm()"""

"""
    A -solve(A,b)
    B - matrix k,l
    x- list of solution [x_1, x_2,..,x_n]
    using Gauss Method
    1.กำจัดจุดอ่อน elimination
    2.แทนคำย้อนกลับ- back substitution
    
    """