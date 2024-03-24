from api import TreeNode, API
from geocoders.geocoder import Geocoder


class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        """
        Перебор дерева для геокодирования area_id.
        """
        node = self.find_node(area_id, self.__data)
        if node:
            address = node.name
            while node.parent_id:
                node = self.find_node(node.parent_id, self.__data)
                if node:
                    address = node.name + ", " + address
                else:
                    return "Unknown"
            return address
        else:
            return "Unknown"

    def find_node(self, area_id: str, nodes: list[TreeNode]) -> TreeNode:
        """
        Поиск узла по area_id в дереве.
        """
        for node in nodes:
            if node.id == area_id:
                return node
            child_node = self.find_node(area_id, node.areas)
            if child_node:
                return child_node
        return None
