import random
#from random import *
#from random import randint
random.seed()
print random.randint(1,15) #losowy wybor od 1 do 15
print random.randint(1,15) #jw
l=range(1,10)
print random.choice(l) #losowy wybor elementu z sekwencji
random.shuffle(l) #losowa permutacja sekwencji
print l
print random.random() #losowa liczba rzeczywista od 0 do 1
print random.uniform(10,30) #losowa liczba rzeczywista od 10 do 30
print random.normalvariate(5,48) #zmienna losowa o rozkladzie normalny o sredniej 5 i odchyleniu 48