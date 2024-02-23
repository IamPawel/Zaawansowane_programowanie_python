"""
Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
tekst "Liczba parzysta" / "Liczba nieparzysta"
"""

def check_num(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
check1 = check_num(34234)

if check1 == True:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")