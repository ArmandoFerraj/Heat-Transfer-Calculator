import numpy as np
from MatrixGenerator import MatrixA
from VectorQ import Vectorq

def HTF():
    T = int(input("number of nodes="))
    area = float(input("Area (m^2)="))
    q0 = float(input("q0 (C)="))
    qf = float(input("qf (C)="))
    A = MatrixA(T,area)
    A = area * A
    InvA = np.linalg.inv(A)
    q = Vectorq(T,q0,qf)
    t = np.matmul(InvA,q)
    t = t - 273.15
    return t
    
t = HTF()
print('temperature=',t)


    

    
  
    
    
    


