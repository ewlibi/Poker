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
  def shuffle(self, times=1 ):
    random.shuffle(self.karte)
    print("Špil izmješan")

  def djeljenje(self):
    return self.karte.pop(0)

class Poker_spil(Spil):
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
              "Dečko":11,
              "Dama":12,
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
        self.karte.append( Karta(ime, vrijednost_karata[ime], boja, simbol) )

  def __repr__(self):
    return "Poker špil: karte:{0} preostalo".format(len(self.karte))

class Igrac(object):
  def __init__(self):
    self.karte = []

  def brojanje_karata(self):
    return len(self.karte)

  def dodaj_kartu(self, karta):
    self.karte.append(karta)


class Pokerrezultat(object):
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
      if vrijednost_karata.brojac(vrijednost) > brojac:
        brojac = vrijednost_karata.brojac(vrijednost)

    return brojac

  def parovi(self):
    parovi = []
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    for vrijednost in vrijednost_karata:
      if vrijednost_karata.brojac(vrijednost) == 2 and vrijednost not in parovi:
        parovi.append(vrijednost)

    return parovi

  def poker(self):
    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    for vrijednost in vrijednost_karata:
      if vrijednost_karata.brojac(vrijednost) == 4:
        return True

  def ful(self):
    dva = False
    tri = False

    vrijednost_karata = [karta.vrijednost for karta in self.karte]
    if vrijednost_karata.brojac(vrijednost_karata) == 2:
      dva = True
    elif vrijednost_karata.brojac(vrijednost_karata) == 3:
      tri = True

    if dva and tri:
      return True

    return False
#unos igraca
#početni saldo, ulog za svaku rundu
