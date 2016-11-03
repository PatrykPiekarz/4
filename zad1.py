#skrypt losujacy 6 unikatowych liczb od 1 do 49
import random
random.seed()
x=random.randint(1,49)
n=set([x])
i=1
while i < 5:
    i+=1
    y=0
    while y==0 :
        x=random.randint(1,49)
        if ( x not in n):
            n.add(x)
            y=1
print n