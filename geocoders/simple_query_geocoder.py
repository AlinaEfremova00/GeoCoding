from api import API
from geocoders.geocoder import Geocoder


class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        address = ""
        while area_id:
            area = API.get_area(area_id)
            address = area.name + ", " + address
            area_id = area.parent_id
        return address.rstrip(", ")

