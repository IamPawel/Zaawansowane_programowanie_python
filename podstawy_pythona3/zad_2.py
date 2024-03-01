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
        book_list = '\n'.join([str(book) for book in self.books])
        return f'Order order handled by: {self.employee.first_name} {self.employee.last_name} \nfor: {self.student} \nbooks: {book_list} \n{self.order_date}' #dopisać książki
    

class Student:
    def __init__(self, first_name, last_name, student_id, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}, id: {self.student_id} born: {self.birth_date}, \nadress: {self.city}, st.{self.street}, zip code:{self.zip_code}, \nphone:{self.phone}'
    

biblioteka1 = Library('Warszawa', 'Marszałkowska', '00-001', '8:00-20:00', '123-456-789')
biblioteka2 = Library('Warszawa', 'Piłsudskiego', '00-002', '9:00-17:00', '987-654-321')

ksiazka1 = Book(biblioteka1, '2020', 'Adam', 'Mickiewicz', 300)
ksiazka2 = Book(biblioteka1, '2019', 'Henryk', 'Sienkiewicz', 400)
ksiazka3 = Book(biblioteka1, '2018', 'Juliusz', 'Słowacki', 400)
ksiazka4 = Book(biblioteka2, '2017', 'Eliza', 'Orzeszkowa', 220)
ksiazka5 = Book(biblioteka2, '2016', 'Stefan', 'Żeromski', 350)

pracownik1 = Employee('Jan', 'Kowalski', '2010-01-01', '1980-01-01', 'Warszawa', 'Marszałkowska', '00-001', '632-456-764')
pracownik2 = Employee('Anna', 'Nowak', '2012-01-01', '1982-01-01', 'Warszawa', 'Róży', '00-001', '767-456-764')
pracownik3 = Employee('Piotr', 'Lewandowski', '2015-01-01', '1985-01-01', 'Warszawa', 'Piłsudskiego', '00-002', '998-123-700')

student1 = Student('Wiktor', 'Nowicki', '123456', '2000-01-01', 'Warszawa', 'Długa', '00-001', '332-223-445')
student2 = Student('Karolina', 'Adamek', '654321', '2002-01-01', 'Warszawa', 'Krótka', '00-001', '778-999-546')
student3 = Student('Kamil', 'Ciemny', '987654', '2001-01-01', 'Warszawa', 'Kręta', '00-002', '757-090-009')

zamowienie1 = Order(pracownik1, student1, [ksiazka1, ksiazka2], '2024-01-21')
zamowienie2 = Order(pracownik3, student2, [ksiazka3, ksiazka4, ksiazka5], '2024-02-22')

print(zamowienie1)
print(zamowienie2)

