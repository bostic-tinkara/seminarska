# main

from lib.poberi import poberi_osnovno, poberi_kriterije, \
                    poberi_kontinente, poberi_znamenitosti
from lib.izlusci import izlusci_osnovno, izlusci_kontinente, \
                    izlusci_opise_kriterijev, izlusci_znamenitosti
from lib.shrani import shrani_csv

def main():
    """
    Izvede glavne funkcije programa: pobere podatke o znamenitostih,
    njihovih lastnostih, kriterijih in kontinentih ter jih shrani v datoteke
    HTML, nato jih izlušči in shrani v različne podatkovne strukture,
    nazadnje pa jih vrne v datoteki CSV.
    """
    poberi_osnovno()
    poberi_kriterije()
    poberi_kontinente()
    znamenitosti = izlusci_osnovno()
    slovar_kont = izlusci_kontinente()
    slovar_krit = izlusci_opise_kriterijev()
    poberi_znamenitosti(znamenitosti)
    podatki = izlusci_znamenitosti(znamenitosti, slovar_kont, slovar_krit)
    shrani_csv(podatki)

if __name__ == "__main__":
    main()