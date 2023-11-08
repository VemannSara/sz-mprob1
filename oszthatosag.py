import math
N = int(input("Írj be egy számot!: "))
i = 2
while (i <= math.sqrt(N)) and (N % i != 0):
    i += 1
van =(i <= math.sqrt(N))
if van:
    O = i
    print("A legkisebb oszto: " + str(O))
    print("A legnagyobb oszto: " + str(N/O))
else:
    print("Prim")

