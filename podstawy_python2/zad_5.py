"""
Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.
"""


def check(list: list, number: int):
    if number in list:
        return True
    else:
        return False


check1 = check([1, 2, 3, 4, 5], 6)
print(check1)
