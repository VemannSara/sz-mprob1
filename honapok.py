H = input("Írj be egy hónap nevet kisbetűvel!: ")
HóNév = ["január","február","március","április","május","június","július","augusztus","szeptember","október","november","december"]
s = 0
while (s<12) and HóNév[s] != H:
    s += 1
print("A " + H + " sorszáma: " + str(s+1))
    