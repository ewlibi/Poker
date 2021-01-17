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
    boje = {"Herz":"♡", "Pik":"♠", "Karo":"♢", "Tref":"♣"}
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

  def __repr__(self):
    return "Špil: karte:{0} preostalo".format(len(self.karte))

class Igrac(object):
  def __init__(self,ime,saldo):
    self.__ime = ime
    self.__saldo = saldo
    self.karte = []
    self.__ulog = 5

  @property
  def ime(self):
    return self.__ime

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
##
##  @property
##  def karte(self):
##    karte_kopija = []
##    for karta in range(len(karte)):
##        karte_kopija.append(karta)
##    return list(karte_kopija)

  def saldo(self, vrijednost):
    self.__saldo = vrijednost
  def broj_karata(self):
    return len(self.karte)

  def dodaj_kartu(self, karta):
    self.karte.append(karta)

  def ima_novaca():
    if self.__saldo <= 0:
        return false

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

#unos igraca
#početni saldo, ulog za svaku rundu
def virtualni_poker():
  igrac = Igrac("Pero",200)

  # Početni iznos
  bodovi = 200

  # Iznos po svakoj ruci
  ruka = 5

  kraj = False
  while not kraj:
    print( "Imate {0} bodova".format(bodovi) )
    print()

    bodovi-=5

    spil = Spil()
    spil.shuffle()

    for i in range(5):
      igrac.dodaj_kartu(spil.djeljenje())

    # Da se vide
    for karta in igrac.karte:
      karta.vidljivo = True
    print(igrac.karte)

    ispravan_unos = False
    while not ispravan_unos:
      print("Koliko karata želite? Zarez nakon svake karte! ( 1, 2, 3 )")
      print("*Prtisnuti return za sve, upišite izlaz za prekid igre")
      uneseni_str = input()

      if uneseni_str == "izlaz":
        kraj=True
        break

      try:
        unos_lista = [int(uns.strip()) for uns in uneseni_str.split(",") if uns]

        for uns in unos_lista:
          if uns > 6:
            continue
          if uns < 1:
            continue

        for uns in unos_lista:
          igrac.karte[uns-1] = spil.djeljenje()
          igrac.karte[uns-1].vidljivo = True

        ispravan_unos = True
      except:
        print("Greška: Između svake karte ide zarez!")

    print(igrac.karte)
    #Rezultat
    rezultat = ProvjeraRuke(igrac.karte)
    skala = rezultat.skala()
    boja_fl = rezultat.boja_fl()
    najveci_broj = rezultat.najveci_broj()
    parovi = rezultat.parovi()

    # royal_flush
    if skala and boja_fl and skala == 14:
      print("Royal flush!!!")
      print("+2000")
      bodovi += 2000

    # skala u boji
    elif skala and boja_fl:
      print("skala u boji!")
      print("+250")
      bodovi += 250

    # Poker
    elif rezultat.poker():
      print("Poker!")
      print("+125")
      bodovi += 125

    # Ful
    elif rezultat.ful():
      print("Ful!")
      print("+40")
      bodovi += 40

    # boja_fl
    elif boja_fl:
      print("boja_fl!")
      print("+25")
      bodovi += 25

    # Skala
    elif skala:
      print("Skala!")
      print("+20")
      bodovi += 20

    # Tris
    elif najveci_broj == 3:
      print("Tris!")
      print("+15")
      bodovi += 15

    # 2 para
    elif len(parovi) == 2:
      print("Dva para!")
      print("+10")
      bodovi += 10

    # 1 par
    elif parovi and parovi[0] > 10:
      print ("Jedan par!")
      print("+5")
      bodovi += 5

    igrac.karte=[]

    print()
    print()