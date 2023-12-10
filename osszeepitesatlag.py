def beolvasas():
    #adatok beolvasása egyszerre és egésszé alakítás
    N,M,K=[int(x) for x in input().split()] 
    adatok = []
    for i in range(N):
        sor=[]
        for j in range(M):
            sor.append(int(input()))
        adatok.append(sor)
    return N,M,K,adatok


N,M,K,adatok=beolvasas()
for i in range(N):
    for j in range(M):
        print(adatok[i][j], end=" ")
    print()


"""Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()"""


