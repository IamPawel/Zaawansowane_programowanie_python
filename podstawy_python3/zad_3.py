"""
Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
    area
    rooms (int)
    price
    address
House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
    plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
    floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę
__str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
tworzenia instancji klasy za pośrednictwem konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je
wyświetlić.
"""


class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area} sq. meters, Rooms: {self.rooms}, Price: ${self.price}, Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {super().__str__()}, Plot size: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {super().__str__()}, Floor: {self.floor}"


house = House(area=200, rooms=5, price=500000, address="123 Main St", plot=600)
flat = Flat(area=100, rooms=3, price=300000, address="456 Elm St", floor=2)

print(house)
print(flat)
