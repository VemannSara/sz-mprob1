M = int(input("Írja be az évet:"))
# lista (tömb)
Szin=["zold","piros","sarga","feher","fekete"]
# // egész osztás
y=((M-1984) % 10) // 2
print(Szin[y])