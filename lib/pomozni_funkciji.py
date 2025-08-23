# pomožni funkciji pri izluščenju podatkov

def opis_kriterija(seznam, slovar):
    """
    Sprejme seznam (kriterijev) in slovar (s kriteriji in z njihovimi opisi)
    ter vrne seznam naborov (kriterijev in opisov).
    """
    dopolnjen = []
    if not seznam:
        return dopolnjen

    for kriterij in seznam:
        dopolnjen.append((kriterij, slovar[kriterij]))
    return dopolnjen

def z_besedo(seznam, slovar):
    """
    Sprejme seznam (kratic kontinentov) in slovar (kratic in imen kontinentov)
    ter vrne seznam (imen kontinentov).
    """
    besedni_sez = []
    if not seznam:
        return ["ni podatka"]

    for kratica in seznam:
        beseda = slovar[kratica]
        besedni_sez.append(beseda)
    return besedni_sez
