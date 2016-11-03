#skrypt ktory dziala jak ksiazka adresowa. dane moga byc dodawane, usuwane i modyfikowane. dane wyswietlane jako tabela

class Adres:
    def __init__(self,pes,imi,naz,adr,kra,num,ema):
        self.pesel=pes
        self.imie=imi
        self.nazwisko=naz
        self.adres=adr
        self.kraj=kra
        self.numer=num
        self.email=ema
    def __lt__(self, other):
        return self.pesel < other.pesel

lst=[]
exit=0
while exit==0:
    x=raw_input('1=dodaj,2=usun,3=modyfikuj,4=wyswietl,5=zakoncz')
    x=int(x)
    y=0
    if(x==1):
        p1=raw_input('podaj pesel:')
        for i in lst:
            if(i.pesel==p1):
                print 'Adresat o tym peselu juz istnieje'
                y=1
                break
        if(y==0):
            p2=raw_input('podaj imie:')
            p3=raw_input('podaj nazwisko:')
            p4=raw_input('podaj adres:')
            p5=raw_input('podaj kraj:')
            p6=raw_input('podaj numer telefonu:')
            p7=raw_input('podaj email:')
            lst.append(Adres(p1,p2,p3,p4,p5,p6,p7))
            print 'Dodano'
    if(x==2):
        p1=raw_input('podaj pesel usuwanego adresata')
        for i in lst:
            if(i.pesel==p1):
                lst.remove(i)
                print 'Usunieto'
                y=1
        if(y==0):
            print 'Nie znaleziono adresata o peselu %s' % (p1)
    if(x==3):
        p1=raw_input('podaj pesel modyfikowanego adresata')
        for i in lst:
            if(i.pesel==p1):
                p2=raw_input('podaj imie: (obecne to %s)' % (i.imie) )
                p3=raw_input('podaj nazwisko: (obecne to %s)' % (i.nazwisko) )
                p4=raw_input('podaj adres: (obecny to %s)' % (i.adres) )
                p5=raw_input('podaj kraj: (obecny to %s)' % (i.kraj) )
                p6=raw_input('podaj numer telefonu: (obecny to %s)' % (i.numer) )
                p7=raw_input('podaj email: (obecny to %s)' % (i.email) )
                i.imie=p2
                i.nazwisko=p3
                i.adres=p4
                i.kraj=p5
                i.numer=p6
                i.email=p7
                print 'Zmodyfikowano'
                y=1
        if(y==0):
            print 'Nie znaleziono adresata o peselu %s' % (p1)
    if(x==4):
        lst.sort()
        print '%10s | %10s | %10s | %10s | %10s | %10s | %20s \n' % ('PESEL','NAZWISKO','IMIE','ADRES,','KRAJ','TELEFON','EMAIL')
        for i in lst:
            print '%10s | %10s | %10s | %10s | %10s | %10s | %20s' % (i.pesel,i.nazwisko,i.imie,i.adres,i.kraj,i.numer,i.email)
    if(x==5):
        exit=1