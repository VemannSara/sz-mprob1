import math
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if (a != 0):
    #masodfokú fgv
    #lassabb a négyzetre emelés
    d = b*b-4*a*c
    van = (d >= 0)
    if (van):
        #van megoldás
        if (d == 0):
            x = (-b)/(2*a)
            print("Egy gyök van: "+ str(x))
        else:
            x1 = ((-b - math.sqrt(d))/(2*a))
            x2 = ((+b - math.sqrt(d))/(2*a))
            print("Egyik gyök:" + str(x1))
            print("Másik gyök:" + str(x2))
    else:
        print("Nincs valos gyok")
else:
    print("Nem masodfoku")