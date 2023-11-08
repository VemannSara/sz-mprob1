N = int(input("Hány nap volt mérés?: "))
M = []
for i in range(N):
    M.append(int(input()))

max = M[0]
for i in range(N):
    if (max < M[i]):
        maxÉrt = M[i]
        maxI = i
print("A " + str(maxI+1) + ". nap a legesősebb")
print("A " + str(maxÉrt) + " a legtöbb eső")

