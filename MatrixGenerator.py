import numpy as np

def MatrixA(T,area):

    

    #Create a list of all the U values 
    ulist = []
    for i in range(1,T):
        k = input(f"thermal conductivity: K{i} =")
        l = input(f"Thickness: L{i} =")
        u = float(k)/float(l)
        ulist.append(u)

    # create a TxT matrix full of zeros
    matrix = np.zeros((T,T))

    #create list of main diagonal indices
    MainDiagonal = []
    for i in range(2,T):
        indi = [i-1,i-1]
        MainDiagonal.append(indi)

    #create list of top diagonal indices
    TopDiagonal = []
    for j in range(2,T):
        indit = [j,j-1]
        TopDiagonal.append(indit)
        
    #create list of bottom diagonal indices
    BottomDiagonal = []
    for z in range(2,T):
        indib = [z-2,z-1]
        BottomDiagonal.append(indib)
        
    #Substitute u values into the main diagonal: (U_n + U_n+1) 
    count = 0 
    for i in MainDiagonal:
        p=i[0]  
        q=i[1] 
        u_n = ulist[count]
        u_nplus1 = ulist[count + 1]
        uval = u_n + u_nplus1
        matrix[p,q]= uval
        count = count + 1

    #substitute u values into the top diagonal: -U_n
    count = 1
    for i in TopDiagonal:
        q = i[0]
        p = i[1]
        uval = ulist[count] * -1
        matrix[p,q] = uval
        count = count + 1
    
    
    #substitute u values into the bottom diagonal: 
    count = 0
    for i in BottomDiagonal:
        q = i[0]
        p = i[1]
        uval = ulist[count] * -1
        matrix[p,q] = uval
        count = count + 1
       
    matrix[0][0] = 1/area
    matrix[T-1][T-1] = 1/area
    return matrix






    
    
    






    

    
  
    
    
    


