import numpy as np
#Exi1
v=np.random.randint(0,101,10)
#print(np.sort(v))
print(v)
def rendezes(v):
    if v.shape[0]==1:
        return True
    if v[0]<=v[1]:
        for i in range(1,v.size-1):
            if v[i]>v[i+1]:
                return False
        return True
    elif v[0]>=v[1]:
        for i in range(1,v.size-1):
            if v[i]<v[i+1]:
                return False
    return True
print(rendezes(v))

#Exi2
def rendezOszlopszerint(m,idx):
    for i in range(0,len(m[:,idx])):
        for j in range(i+1,len(m[:,idx])):
            if m[i,idx]<m[j,idx]:
                tmp=m[i,:].copy()
                m[i,:]=m[j,:].copy()
                m[j,:]=tmp.copy()
# tömbből másolni nem lehet így ,tömb részeit, tömböt nem lehet csak a copy metódussal

v=np.random.randint(0,101,(4,5))
print(v)
rendezOszlopszerint(v,2)
print(v)

#Exi3
def osszeg(m):
    s=0
    o=0
    for i in range(m.shape[0]-1):
        for j in range(m.shape[0]-1):
            s=m[i][j]+s
    for i in range(m.shape[1]-1):
        for j in range(m.shape[0]-1):
            o=m[i][j]+o
    if s==o:
        return True
    else:
        return False
m = np.random.randint(0,101,(4,5))
print(m)
print(osszeg(m))
d=np.array(([1,1,1],[1,1,1],[1,1,1]))
print(d)
print(osszeg(d))

#Exi4
def nulla(m):
    index=[]
    for j in range(m.shape[1]):
        zero = 0
        n=0
        for i in range(m.shape[0]):
            if m[i][j]<0:
                n=n+1
            if m[i][j]==0:
                zero=zero+1
        if 2*n>=zero:
            index.append(j)
    return index
m = np.random.randint(-10,10,(4,5))
print(m)
print(nulla(m))
v=np.array(([0,-3,0],[0,-8,0],[-8,-8,0],[-1,-3,0]))
print(v)
print(nulla(v))

#Exi5
def osztogatas(m):
    indexi=[]
    indexj=[]
    for j in range(1,m.shape[1]):
        for i in range(1,m.shape[0]):
            if m[i-1][j-1]%i==0 and m[i-1][j-1]%j==0:
                indexi.append(i)
                indexj.append(j)
    return indexi,indexj
m = np.random.randint(-10,10,(4,5))
print(m)
index1,index2=osztogatas(m)
print(index1)
print(index2)
v=np.array(([11,11,11],[11,11,11],[11,11,11],[11,11,11]))
print(v)
index1,index2=osztogatas(v)
print (index1)
print(index2)
