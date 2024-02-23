"""
Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.
"""

def list_operation(a: list, b: list):
    newlist = list(a + b)
    newlist = list(set(newlist))
    newlist = [i**3 for i in newlist]
    print(newlist)

list_operation([1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7])