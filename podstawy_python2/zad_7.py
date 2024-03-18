"""
Stworzyć skrypt pythonowy, który połączy się z API, które
zawiera informacje o browarach (dokumentacja
https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę
Brawery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę
__str__ która będzie opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy
Brawery , którą przeiteruje i wyświetli każdy obiekt z osobna.
"""

import requests


class Brewery:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.brewery_type = data["brewery_type"]
        self.street = data["street"] if "street" in data else None
        self.city = data["city"]
        self.state = data["state"]
        self.postal_code = data["postal_code"]
        self.country = data["country"]
        self.phone = data["phone"] if "phone" in data else None
        self.website_url = data["website_url"] if "website_url" in data else None

    def __str__(self):
        return f"Brewery name: {self.name}, type: {self.brewery_type}, adress: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}, \nWebsite: {self.website_url}"

    def fetch_breweries():
        response = requests.get("https://api.openbrewerydb.org/breweries")
        data = response.json()[:20]
        breweries = []
        for brewery in data:
            breweries.append(Brewery(brewery))
        return breweries

beweries = Brewery.fetch_breweries()
for bewery in beweries:
    print(bewery)
