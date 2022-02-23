class Kutya:
    def __init__(self, nev, fajta, eletkor):
        self.nev = nev
        self.fajta = fajta
        self.eletkor = int(eletkor)


def kutyalista():
    kutyak = []
    print('Add meg rendre a kutyák adatait!')
    print('(Ha valamelyiket üresen hagyod, a bekérés befejeződik.)')
    no = 1
    while True:
        print(f'add meg az {no}. kutya adatait!')
        n = input('\tneve: ')
        if len(n) == 0: break
        f = input('\tfajtája: ')
        if len(f) == 0: break
        k = input('\tkora: ')
        if len(k) == 0: break
        kutyak.append(Kutya(n, f, k))
        no += 1
    return kutyak


def vizslak_szama(kutyak):
    c = 0
    for k in kutyak:
        if k.fajta.lower() == 'vizsla':
            c += 1
    return c


def legoregebb_kutya_fajtaja(kutyak):
    maxi = 0
    for i in range(1, len(kutyak)):
        if kutyak[i].eletkor > kutyak[maxi].eletkor:
            maxi = i
    return kutyak[maxi].fajta


def osszes_T_fajtaju(kutyak, ker_fajta):
    kutyanevek = []
    for k in kutyak:
        if k.fajta.lower() == ker_fajta.lower():
            kutyanevek.append(k.nev)
    if len(kutyanevek) == 0:
        print(f'nincs {ker_fajta} fajtájú kutya')
    else: print(f'{kutyanevek} mind {ker_fajta}')