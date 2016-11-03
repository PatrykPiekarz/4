#skrypt ktory bedzie zgadywal liczbe, losuje z zakresu uzytkownika (uzytkownik podaje liczbe, program mowi czy za male czy za duze), okreslona ilosc zgadnien
import random

n=raw_input('podaj zakres od 0 do:')
n=int(n)
z=0
random.seed()
x=random.randint(0,n)
y=raw_input('podaj liczbe: (-1 konczy gre)')
y=int(y)
while 0==0:
    if(y==-1):
        break
    z=0
    for i in range(0,5):
        if(y==x):
            z=1
            break
        if(y<x):
            y=raw_input('liczba za mala, sproboj jeszcze raz')
            y=int(y)
        if(y>x):
            y=raw_input('liczba za duza, sproboj jeszcze raz')
            y=int(y)
    if(y==x):
        z=1
    if(z==0):
        random.seed()
        x=random.randint(0,n)
        y=raw_input('wykorzystano proby, losuje nowa liczbe, podaj liczbe: (-1 konczy gre)')
    if(z==1):
        n=raw_input('zgadles liczbe, podaj nowy zakres:')
        n=int(n)
        random.seed()
        x=random.randint(0,n)
        y=raw_input('podaj liczbe: (-1 konczy gre)')
        y=int(y)