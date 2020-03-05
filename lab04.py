import numpy as np

#Exi 1
v=np.arange(0,50)
v=v[::-1]

print(v)

#Exi2
v=np.array(np.round(100*np.random.random(30)), dtype=np.uint8)
min=np.min(v)
max=np.max(v)
indices=np.where((v==max) | (v==min) )
print(v)
print(max)
print(min)
print(indices)

#Exi3
v=np.array(np.round(100*np.random.random(10)), dtype=np.uint8)
min=np.min(v)
max=np.max(v)
indices=np.where((v==max) | (v==min) )
print(v)
print(max)
print(min)
print(indices)
print(v[indices])


#Exi 4*-nem jó
#def sort_vector(v):
#   min=0
#    for i in range(v.shape[0]):
#       for j in range(i+1,v.shape[0]):
#            if v[i]>v[j]:
#               v[i],v[j]=v[j],v[i]
#  return v
#import time
#v=np.random.randint(1,20,150)
#print(v)
#start=time.time()
#v=sort_vector(v)
#end=time.time()
#print(end-start)

#Exi 5
v=np.random.randint(1,10,120)
#indices=np.where((v>=3) &(v<=8))
print(v)
v[(v>=3) &(v<=8)]*=-1
print(v)

#Exi 6
v=np.random.randint(1,20,10)
