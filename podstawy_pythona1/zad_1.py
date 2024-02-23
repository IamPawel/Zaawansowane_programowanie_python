"""
Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
wyświetli każde z nich.
"""

names = ["Paweł", "Kasia", "Ania", "Piotrek", "Kuba"]

def wyswietl_imiona(names):
    for i in names:
        print(i)

wyswietl_imiona(names)


"""
Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
zwróci. Zadanie należy wykonać w 2 wersjach:
1. Wykorzystując pętle for .
2. Wykorzystując listę składaną.
"""

def multipy_by_2(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    print(numbers)

num = [20, 12, 93, 44, 35]
multipy_by_2(num)

num2 = [23, 52, 493, 1244, 345]
def multipy_by_2_v2(numbers):
    numbers = [i*2 for i in numbers]
    print(numbers)

multipy_by_2_v2(num2)

"""
Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
jedynie parzyste elementy.
"""
numlist = list(range(1, 11))
print(numlist)
def even_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)
    
even_numbers(numlist)

"""
Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range), a następnie wyświetli co
drugi element.
"""
seclist = list(range(1, 21))
def every_two(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])
every_two(seclist)
