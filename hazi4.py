import sys
def elofordulas(s,k):
    db=0
    for ch in s:
        if ch==k:
            db=db+1
    return db
print(elofordulas(sys.argv[1],sys.argv[2]))