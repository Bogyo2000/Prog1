import sys
def atalakito(n):
    n=int(n)
    ido=n
    ev=n//(3600*24*365)
    n=n%(3600*24*365)
    nap=n//(3600*24)
    n=n%(3600*24)
    ora=n//3600
    n=n%3600
    perc=n//60
    ms=n%60
    print(ev,nap,ora,perc,ms )
atalakito(sys.argv[1])