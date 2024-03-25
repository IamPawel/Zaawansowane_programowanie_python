"""
Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
ocen jest > 50% (2,5) w przeciwnym przypadku negatywną. Następnie należy
stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
zwracała true , a dla drugiego false .
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks) / len(self.marks) > 2.5:
            return True
        else:
            return False


student1 = Student("Paweł", [3, 4, 5, 3, 4])
print(student1.is_passed())
student2 = Student("Kasia", [2, 3, 2, 2, 2])
print(student2.is_passed())
