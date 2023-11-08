x=["alma","körte","szilva"]
print(x)

for szó in x:
    print(szó,end=":")
print(":".join(x))

try:
    print(3/0)
except:
    print("hiba")

l=["alma",4,"szilva"]
# a 0. és az 1. elmet kivágom
print(l[:2])
l.append(7)
print(l)
# elem felülírás
l[1] = 17
print(l)
# tuple, nem lehet felülírni az elemeit
t=("alma",4,"szilva")
print(t[0])

y=[0]*10
print(y)




