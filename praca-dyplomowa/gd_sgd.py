# Prosty spadek wzdluz gradientu
while True:
    wagi_gradientu = sprawdz_gradient(funkcja_kosztu, dane, wagi)
    wagi -= tempo_uczenia * wagi_gradientu

# Stochastyczny spadek wzdluz gradientu
while True:
    probka = probkuj_zbior(dane, 256) # Losuje 256 przykladow ze zbioru danych. Potegi 2 sa uzywane zwyczajowo
    wagi_gradientu sprawdz_gradient(funkcja_kosztu, probka, wagi)
    wagi -= tempo_uczenia * wagi_gradientu