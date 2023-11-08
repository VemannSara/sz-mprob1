mgh = "aáeéiíöőuúüű"
szo = input()
szo = szo.lower()

i=0
while szo[i] not in mgh:
    i += 1
mgh = szo[i]

print(mgh)
