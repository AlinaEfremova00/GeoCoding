from api import TreeNode, API
from geocoders.geocoder import Geocoder

class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_area()
        else:
            self.__data = data
        self.__addresses = {}

        # Вызываем _collect_addresses для каждого узла дерева
        for node in self.__data:
            self._collect_addresses(node)

    def _collect_addresses(self, node: TreeNode, path: str = "") -> None:
        path = node.name + ", " + path
        self.__addresses[node.id] = path.rstrip(", ")
        for child in node.areas:
            self._collect_addresses(child, path)

    def _apply_geocoding(self, area_id: str) -> str:
        return self.__addresses.get(area_id, "Unknown")
