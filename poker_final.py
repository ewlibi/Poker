import random

class Karta( object ):
  def __init__(self, ime, vrijednost, boja, simbol):
    self.vrijednost = vrijednost
    self.boja = boja
    self.ime = ime
    self.simbol = simbol
    self.vidljivo = False

  def __repr__(self):
    if self.vidljivo:
      return self.simbol
    else:
      return "Karta"

class Spil(object):
  def __init__(self):
    self.karte = []
    boje = {"Herz":"♥", "Pik":"♠", "Karo":"♦", "Tref":"♣"}
    vrijednost_karata = {"Dvica":2,
              "Trica":3,
              "Četvorka":4,
              "Petica":5,
              "Šestica":6,
              "Sedmica":7,
              "Osmica":8,
              "Devetka":9,
              "Desetka":10,
              "JDečko":11,
              "QDama":12,
              "Kralj":13,
              "As":14 }

    #prikaz simbola
    for ime in vrijednost_karata:
      for boja in boje:
        simbol_ikone = boje[boja]
        if vrijednost_karata[ime] < 11:
          simbol = str(vrijednost_karata[ime])+simbol_ikone
        else:
          simbol = ime[0]+simbol_ikone
        self.karte.append(Karta(ime, vrijednost_karata[ime], boja, simbol) )

  def shuffle(self, times=1):
    random.shuffle(self.karte)
    print("Špil izmješan")

  def djeljenje(self):
    return self.karte.pop(0)

class Igrac(object):
  def __init__(self,ime = "Igrac"):
    self.__ime = ime
    self.__saldo = 1
    self.karte = []
    self.__ulog = 5

  @property
  def ime(self):
    return self.__ime

  @ime.setter
  def ime(self, value): self.__ime = value

  @property
  def saldo(self):
    return self.__saldo

  @property
  def ulog(self):
    return self.__ulog

  @ulog.setter
  def ulog(self, vrijednost):
    self.__ulog = vrijednost

  @saldo.setter
  def saldo(self, vrijednost):
    self.__saldo = vrijednost

  def saldo(self):
    return self.__saldo
  def broj_karata(self):
    return len(self.karte)

  def dodaj_kartu(self, karta):
    self.karte.append(karta)

class ProvjeraRuke(object):
  def __init__(self, karte):
    # Broj karte
    if not len(karte) == 5:
      return "Greška: Pogrešan broj karte"
    self.karte = karte

  def boja_fl(self):
    boje = [karta.boja for karta in self.karte]
    if len( set(boje) ) == 1:
      return True
    return False

  def skala(self):
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    vrijednost_karata.sort()

    if not len( set(vrijednost_karata)) == 5:
      return False

    if vrijednost_karata[4] == 14 and vrijednost_karata[0] == 2 and vrijednost_karata[1] == 3 and vrijednost_karata[2] == 4 and vrijednost_karata[3] == 5:
      return 5

    else:
      if not vrijednost_karata[0] + 1 == vrijednost_karata[1]: return False
      if not vrijednost_karata[1] + 1 == vrijednost_karata[2]: return False
      if not vrijednost_karata[2] + 1 == vrijednost_karata[3]: return False
      if not vrijednost_karata[3] + 1 == vrijednost_karata[4]: return False

    return vrijednost_karata[4]

  def jaka_karta(self):
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    jaka_karta = None
    for karta in self.karte:
      if jaka_karta is None:
        jaka_karta = karta
      elif jaka_karta.vrijednost < karta.vrijednost:
        jaka_karta=karta

    return jaka_karta

  def najveci_broj(self):
    brojac = 0
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    for vrijednost in vrijednost_karata:
      if vrijednost_karata.count(vrijednost) > brojac:
        brojac = vrijednost_karata.count(vrijednost)

    return brojac

  def parovi(self):
    parovi = []
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    for vrijednost in vrijednost_karata:
      if vrijednost_karata.count(vrijednost) == 2 and vrijednost not in parovi:
        parovi.append(vrijednost)

    return parovi

  def poker(self):
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    for vrijednost in vrijednost_karata:
      if vrijednost_karata.count(vrijednost) == 4:
        return True

  def ful(self):
    dva = False
    tri = False

    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    if vrijednost_karata.count(vrijednost_karata) == 2:
      dva = True
    elif vrijednost_karata.count(vrijednost_karata) == 3:
      tri = True

    if dva and tri:
      return True
    return False

class Igra(object):
    def __init__(self, prikaz = None):
        self.__prikaz = prikaz
        self.__spil = Spil()
        self.__pocetniS = 100
        self.__saldoZaBodovanje = 100
        self.__brDjeljenja = 0
        self.__dobitak = 1
        self.__krajIgre = False

    @property
    def krajIgre(self): return self.__krajIgre
    @krajIgre.setter
    def krajIgre(self, value): self.__krajIgre = value
    @property
    def dobitak(self): return self.__dobitak

    @dobitak.setter
    def dobitak(self, value): self.__dobitak = value

    @property
    def pocetniS(self): return self.__pocetniS


    @pocetniS.setter
    def pocetniS(self, value): self.__pocetniS = value

    @property
    def prikaz(self): return self.__prikaz

    @property
    def spil(self): return self.__spil

    @spil.setter
    def spil(self, value): self.__spil = value

    @property
    def saldoZaBodovanje(self): return self.__saldoZaBodovanje

    @property
    def brDjeljenja(self): return self.__brDjeljenja

    @brDjeljenja.setter
    def brDjeljenja(self, value): self.__brDjeljenja = value

    def igranjePokera(self):
        self.prikaz.prikaziPocetakIgre()    #0
        self.unosIgraca()                   #1
        self.pocetniSaldo()                 #2
        while self.krajIgre == False:
            self.ulog()                         #3
            self.dijeljenjeKarata()             #4
            self.odbacivanjeKarata()            #5
            self.provjeriRuku()                 #6
            self.provjeraSalda()                #7

    def unosIgraca(self):
        ime = self.prikaz.unesiIgraca()
        igrac.ime = ime

    def pocetniSaldo(self):
        pS = self.prikaz.pocetniSaldo()
        saldoZaBodovanje = pS
        igrac.saldo = pS

    def ulog(self):
        ulog = self.prikaz.ulog()
        s = igrac.saldo
        igrac.saldo = s - ulog             #3.3

    def dijeljenjeKarata(self):
        self.spil = Spil()
        self.spil.shuffle()                 #4.1
        for i in range(5):                  #4.2
            igrac.dodaj_kartu(self.spil.djeljenje())

        # Da se vide karte
        for karta in igrac.karte:
            karta.vidljivo = True
        print(igrac.karte)

    def provjeriRuku(self):
        rezultat = ProvjeraRuke(igrac.karte)
        skala = rezultat.skala()            #6.1
        boja_fl = rezultat.boja_fl()
        najveci_broj = rezultat.najveci_broj()
        parovi = rezultat.parovi()

        #6.2

        # royal_flush
        if skala and boja_fl and skala == 14:
            self.dobitak = igrac.ulog*400
            print("Royal flush!!!")
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += (self.dobitak)

        # skala u boji
        elif skala and boja_fl:
            print("skala u boji!")
            self.dobitak = igrac.ulog*50
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += (self.dobitak)

        # Poker
        elif rezultat.poker():
            print("Poker!")
            self.dobitak = igrac.ulog*25
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += (self.dobitak)

        # Ful
        elif rezultat.ful():
            print("Ful!")
            self.dobitak = igrac.ulog*8
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += (self.dobitak)

        # boja_fl
        elif boja_fl:
            print("boja_fl!")
            self.dobitak = igrac.ulog*5
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += (self.dobitak)

        # Skala
        elif skala:
            print("Skala!")
            self.dobitak = igrac.ulog*4
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += self.dobitak

        # Tris
        elif najveci_broj == 3:
            self.dobitak = igrac.ulog*3
            igrac.saldo += self.dobitak
            print("Tris!")
            print("+" + str(self.dobitak) + " bodova!")


        # 2 para
        elif len(parovi) == 2:
            self.dobitak = igrac.ulog*2
            print("Dva para!")
            print("+" + str(self.dobitak) + " bodova!")
            igrac.saldo += (self.dobitak)

        # 1 par
        elif parovi and parovi[0] > 10:
            print ("Jedan par!")
            self.dobitak = igrac.ulog
            print("+" + str(igrac.ulog) + " bodova!")
            igrac.saldo += self.dobitak
        else:
            print("Niste pogodili niti jednu dobitnu kombinaciju!")
        print("_"*50)
        igrac.karte=[]

        s = igrac.saldo                 #6.3
        self.prikaz.promjenaBodova(s)

    def odbacivanjeKarata(self):

        ispravnoOdbacivanje = False
        while ispravnoOdbacivanje == False:
            odluka = self.prikaz.odbacivanjeKarata()         #5.2
            if odluka[0] == 'n':
                break
            try:
                odabirLista = [int(unos) for unos in odluka.split(",")]

                for unos in odabirLista:
                    igrac.karte[unos-1] = self.spil.djeljenje()     #5.1
                    #igrač dobiva nove karte
                    igrac.karte[unos-1].vidljivo = True
                    ispravnoOdbacivanje = True
                    ##print(igrac.karte)
            except: print("Pogrešan unos! ")
    def provjeraSalda(self):
        krajIgre = False
        s = self.saldoZaBodovanje
        if igrac.saldo <= 0:
            print("Igrač je izgubio!")
            self.krajIgre = True
        elif igrac.saldo > s*100:
            print("Igrač je pobijedio! Bravo!!!")
            self.krajIgre = True
        else : self.krajIgre = False

class PrikazIgre(object):

    def prikaziPocetakIgre(self):
        print("#" * 50)
        print("#" * 20 + "Video Poker" + "#" * 19)
        print("#" * 50)

    def unesiIgraca(self):
        while True:
            ime =input("Unesi ime: \n")     #1.1
            if ime.strip():                 #1.2
                print("_"*50)
                return ime.strip()
    def odbacivanjeKarata(self):            #5.1
            odluka = input("Koje karte zelite odbaciti?\nAko zelite zadrzati sve karte upišite 0\nOdabir karata odvojite zarezom (npr. 1,2,3)  ")
            return odluka

    def ulog(self):
        while True:         #3.1
            ulog = input("Koliko želite uložiti za sljedeću rundu?   ")
            try:
                ulog = int(ulog)
                if ulog <= igrac.saldo and ulog > 0:
                    igrac.ulog = ulog
                    return ulog

            except:
                print("Niste unijeli ispravan broj!")


    def pocetniSaldo(self):
        while True:
            #2.1 #2.2
            pocetniSaldo = input("S koliko novaca zelite zapoceti igru?\nNajmanji saldo je 100, a najveći 1000   ")
            try:
                pocetniSaldo = int(pocetniSaldo)
                if pocetniSaldo >= 100 and pocetniSaldo <= 1000: #2.3
                    igrac.saldo = pocetniSaldo
                    return pocetniSaldo
            except:
                print("Niste unijeli ispravan broj!")

    def promjenaBodova(self, saldo):
        print("{0} trenutno ima {1} bodova.".format(igrac.ime,saldo))

pi = PrikazIgre()
igrac = Igrac()
i = Igra(pi)
i.igranjePokera()
