def leghosszabb(file):
    legh=[]
    l=0
    for reader in file:
        sor=reader.split(' ')
        for x in sor:
            szo=x.strip('.,!?"')
            if l<len(szo):
                legh.clear()
                l=len(szo)
            if l==len(szo):
                legh.append(szo)
    return legh,l
try:
    file = open("input.txt", "r")
    print(leghosszabb(file))
except FileNotFoundError:
    print("Nem talalható a fájl")
