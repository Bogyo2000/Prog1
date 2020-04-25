import math
import datetime
#Exi 1
terulet=lambda r:r**2*math.pi
l=[2,4,5,6,8,9]
print(list(map(terulet,l)))

#Exi 2
oszthato=lambda x: True if x%2==0 and x%3==0 else False
print(list(filter(oszthato,l)))

#Exi 3
nevfordito=lambda fn,ln:fn[::-1]+" "+ln[::-1]
fn=input("Mi a keresztneved?")
ln=input("Mi a vezetékneved?")
print(nevfordito(fn,ln))

#Exi 4
ertek=lambda n:n+n*10+n+n*100+n
print(list(map(ertek,[1,2,3,4,5,6,7,8])))

#Exi 5
kulonbseg=lambda y1,m1,d1,y2,m2,d2 : str((datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).days) + ' days'
print(kulonbseg(1996,7,20,2000,1,18))