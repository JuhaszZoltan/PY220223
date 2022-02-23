import modul as m

kutyamenhely = m.kutyalista()

# teszt:
print(f'a menhelyen {len(kutyamenhely)} kutyus van')

# 1. feladat:
print(f'a vizylák száma a menhelyen: {m.vizslak_szama(kutyamenhely)}')

# 2. feladat:
print(f'a legöregebb kutya egy {m.legoregebb_kutya_fajtaja(kutyamenhely)}')

# 3. feladat:
fajta = input('milyen fajtájú kutyát keresel? ')
m.osszes_T_fajtaju(kutyamenhely, fajta)