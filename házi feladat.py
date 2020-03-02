def cserelo(file):
    xfile=open("output.txt",'w')
    for mfile in file:
        for reader in mfile:
            if reader.isupper():
                print(reader.lower(), end="", file=xfile)
            elif reader.islower():
                print(reader.upper(),end="",file=xfile)
            else:
                print(reader,end="",file=xfile)
try:
    file=open("input.txt","r")
    cserelo(file)
except FileNotFoundError:
    print("Nem talalhato a fajl")
