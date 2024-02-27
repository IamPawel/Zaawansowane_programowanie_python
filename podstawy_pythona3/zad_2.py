"""
Stworzyć następujące klasy:
    Library (klasa opisująca bibliotekę), posiadająca pola:
        city
        street
        zip_code
        open_hours (str)
        phone
    Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
        first_name
        last_name
        hire_date
        birth_date
        city
        street
        zip_code
        phone
    Book (klasa opisująca książkę), posiadająca pola:
        library
        publication_date
        author_name
        author_surname
        number_of_pages
    Order (klasa opisująca zamówienie), posiadająca pola:
        employee
        student
        books (lista obiektów klasy Book)
        order_date
Dodatkowo:
Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie
opisywała obiekt oraz ewentualne obiekty znajdujące się w tym obiekcie
(np. obiekt Library w obiekcie Book).
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
tworzenia instancji klasy za pośrednictwem konstruktora.
Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3
studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )
"""

class Library:
    def __init__ (self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library adress: {self.city}, st.{self.street}, zip code:{self.zip_code}, \n.Is open {self.open_hours}, \nphone:{self.phone}'
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}, hired: {self.hire_date}, born: {self.birth_date}, \nadress: {self.city}, st.{self.street}, zip code:{self.zip_code}, \nphone:{self.phone}'

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Book: {self.author_name} {self.author_surname}, published: {self.publication_date}, \n{self.number_of_pages} pages, in library: {self.library} st.{self.library.street} {self.library.city} {self.library.zip_code} \nphone:{self.library.phone}'

class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Order: {self.employee} \n{self.student} \n{self.books} \n{self.order_date}'