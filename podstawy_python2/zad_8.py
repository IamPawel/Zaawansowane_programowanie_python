"""
Dla chętnych Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city ,
który może być przekazywany w wierszu poleceń podczas wykonywania (np.
python main.py --city=Berlin ). Należy wykorzystać moduł argparse do
wczytywania przekazywanych parametrów, a w razie przekazania wartości
ograniczyć pobierane browary do miasta, które zostało wskazane.
"""

import argparse
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
        return f"Brewery name: {self.name}, type: {self.brewery_type}, address: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}, \nWebsite: {self.website_url}"

    @staticmethod
    def fetch_breweries(city=None):
        url = "https://api.openbrewerydb.org/breweries"
        if city:
            url += f"?by_city={city}"
        response = requests.get(url)
        data = response.json()[:20]
        breweries = [Brewery(brewery) for brewery in data]
        return breweries


def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch breweries from Open Brewery DB")
    parser.add_argument("--city", help="Filter breweries by city")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    breweries = Brewery.fetch_breweries(args.city)
    for brewery in breweries:
        print(brewery)
