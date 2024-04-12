from geopy.geocoders import Nominatim
from time import sleep


def get_location(address):
    locator = Nominatim(user_agent="Mozilla/5.0", timeout=5)
    location = locator.geocode(address)
    coordinates = f'{location.latitude}, {location.longitude}'
    return coordinates


def reverse_location(coordinates):
    locator = Nominatim(user_agent="Mozilla/5.0", timeout=5)
    location = locator.reverse(coordinates)

    try:
        city = location.raw["address"]["city"]
    except KeyError:
        city = ""

    country = location.raw["address"]["country"]

    return ", ".join([country, city])
