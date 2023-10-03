import numpy as np
def Vectorq(T,q0,qf):
    q = np.array([0]*(T))
    q[0]=float(q0+273.15)
    q[T-1]=float(qf+273.15)
    return q



