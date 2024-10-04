def cartesian():    
    n = int(input("\nEnter number of elements in first set (A): "))
    A = []
    B = []
    print("Enter elements for A:") 
    for i in range(0, n): 
        ele = float(input()) 
        A.append(ele)
    m = int(input("\nEnter number of elements in second set (B): "))
    print("Enter elements for B:") 
    for i in range(0, m): 
        ele = float(input()) 
        B.append(ele)
    print("A = {"+str(A)[1:-1]+"}")
    print("B = {"+str(B)[1:-1]+"}")
    cart_prod = []
    cart_prod = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            cart_prod[i][j] = min(A[i],B[j])
    print("A x B = ")
    for i in range(n):
        for j in range(m):
            print(cart_prod[i][j],end="  ")
        print("\n")
    return

def fuzzyunion():
    A = []
    B = []
    Y = {}

    n = int(input("\nEnter number of elements in first set (A): "))
    print("Enter elements for A:") 
    """for i in range(0, n): 
        ele = float(input()) 
        A.append(ele)"""
    A = [float(input()) for _ in range(n)]    

    m = int(input("\nEnter number of elements in second set (B): "))
    print("Enter elements for B:") 
    """for i in range(0, m): 
        ele = float(input()) 
        B.append(ele)"""
    B = [float(input()) for _ in range(n)]    
    print('The First Fuzzy Set is :', A)
    print('The Second Fuzzy Set is :', B)

    # Iterate over both sets simultaneously using zip
    for x, y in zip(A, B):
        if x > y:
           Y[x] = x
        else:
           Y[y] = y

    print('Fuzzy Set Union is :', Y)  # Print Y as a dictionary, not float
    return

   
        
def maxmin():
    r1 = int(input("Enter number of rows of first relation (R1): "))
    c1 = int(input("Enter number of columns of first relation (R1): "))
    rel1=[[0 for i in range(c1)]for j in range(r1)]
    print("Enter the elments for R:")
    for i in range(r1):
        for j in range(c1):
            rel1[i][j]=float(input())
    
    r2 = int(input("Enter number of rows of second relation (R2): "))
    c2 = int(input("Enter number of columns of second relation (R2): "))
    rel2=[[0 for i in range(c2)]for j in range(r2)]
    print("Enter the elments for R:")
    for i in range(r2):
        for j in range(c2):
            rel2[i][j]=float(input())
    
    print("\nR1 = ")
    for i in range(r1):
        for j in range(c1):
            print(rel1[i][j],end=" ")
        print("\n")
    print("\nR2 = ")
    for i in range(r2):
        for j in range(c2):
            print(rel2[i][j],end=" ")
        print("\n")
    
    
    col=0
    comp=[]
    for i in range(r1):
        comp.append([])
        for j in range(c2):
            l=[]
            for k in range(r2):
                l.append(min(rel1[i][k],rel2[k][j]))
            comp[i].append(max(l))  
    
    print("\nR1 composition R2 =")
    for i in range(r1):
        for j in range(c2):
            print(comp[i][j],end=" ")
        print("\n")
    return

def intersect():
    A = []
    B = []
    Y = {}
    n = int(input("\nEnter number of elements in first set (A): "))
    print("Enter elements for A:") 
    A = [float(input()) for _ in range(n)]    

    m = int(input("\nEnter number of elements in second set (B): "))
    print("Enter elements for B:") 
    B = [float(input()) for _ in range(n)]
    
    print('The First Fuzzy Set is :', A)
    print('The Second Fuzzy Set is :', B)
    
    # Iterate over both sets simultaneously using zip
    for x, y in zip(A, B):
        if x < y:
           Y[x] = x
        else:
           Y[y] = y

    print('Fuzzy Set INTERSECTION is :', Y)  # Print Y as a dictionary, not float
    return

def complement():
    A = []
    Y = []
    n = int(input("\nEnter number of elements in first set (A): "))
    print("Enter elements for A:") 
    A = [float(input()) for _ in range(n)]    
    
    print('The Fuzzy Set is :', A)
    
    for x in A:                         
        Y.append(1 - x)
       
    print('Fuzzy Set COMPLEMENT is :', Y)  
    return

def fuzzydifference():    #(A-B) means min(A,B) in Fuzzy which means intersection of both
    A = []
    B = []
    dB = []
    Y = {}
    n = int(input("\nEnter number of elements in first set (A): "))
    print("Enter elements for A:") 
    A = [float(input()) for _ in range(n)]    

    m = int(input("\nEnter number of elements in second set (B): "))
    print("Enter elements for B:") 
    B = [float(input()) for _ in range(n)]

    #for difference
    for d in B:
        dB.append(1 - d)
    
    print('The First Fuzzy Set is :', A)
    print('The Second Fuzzy Set is :', B)
    print('The difference of fuzzy set B is :',dB)
    
    # Iterate over both sets simultaneously using zip
    for x, y in zip(A, dB):
        if x < y:
           Y[x] = x
        else:
           Y[y] = y

    print('Fuzzy Set difference (A-B) is :', Y)  # Print Y as a dictionary, not float
    return

def max_Product():
    r1 = int(input("Enter number of rows of first relation (R1): "))
    c1 = int(input("Enter number of columns of first relation (R1): "))
    rel1=[[0 for i in range(c1)]for j in range(r1)]
    print("Enter the elments for R:")
    for i in range(r1):
        for j in range(c1):
            rel1[i][j]=float(input())
    
    r2 = int(input("Enter number of rows of second relation (R2): "))
    c2 = int(input("Enter number of columns of second relation (R2): "))
    rel2=[[0 for i in range(c2)]for j in range(r2)]
    print("Enter the elments for R:")
    for i in range(r2):
        for j in range(c2):
            rel2[i][j]=float(input())
    
    print("\nR1 = ")
    for i in range(r1):
        for j in range(c1):
            print(rel1[i][j],end=" ")
        print("\n")
    print("\nR2 = ")
    for i in range(r2):
        for j in range(c2):
            print(rel2[i][j],end=" ")
        print("\n")
    
    
    col=0
    comp=[]
    for i in range(r1):
        comp.append([])
        for j in range(c2):
            l=[]
            for k in range(r2):
                l.append(rel1[i][k]*rel2[k][j])
            comp[i].append(max(l))  
    
    print("\nR1 product composition R2 =")
    for i in range(r1):
        for j in range(c2):
            print(comp[i][j],end=" ")
        print("\n")
    return

ch=1
while ch==1:
    print("MENU:\n----\n1->Cartesian Product\n2->Max-Min Composition\n3->Union of Fuzzy\n4->Intersection of union\n5->Complement of Fuzzy\n6->Fuzzy Difference\n7->Max-Product of Fuzzy\n8->Exit")
    op=int(input("Enter Your Choice: "))
    if op==1:
        cartesian()
    elif op==2:
        maxmin()
    elif op==3:
        fuzzyunion()
    elif op==4:
        intersect()
    elif op==5:
        complement()
    elif op==6:
        fuzzydifference()
    elif op==7:
        max_Product()
    elif op==8:
        break
    else:
        print("Wrong Choice!")
    ch=int(input("Do you wish to continue (1-Yes | 0-No): "))
    print("\n")
