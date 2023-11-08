N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

db = 0
for i in range(N):
    if (M[i] > 0):
        db += 1

print(db)




    
