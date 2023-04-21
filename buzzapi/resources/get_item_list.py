from urllib.parse import urlencode
from typing import List


class GetItemList:
    def get_item_list(self, entityid: int, params: dict = {}) -> List[dict]:
        """This command lists items.

        Args:
            entityid (int): ID of the course that owns the manifest.
            params (dict):
                itemid: Optional ID of the item to retrieve.
                query:  Optional query used to filter the list of items to retrieve.

        Returns:
            List[dict]: List of Items (https://api.agilixbuzz.com/docs/#!/Schema/ItemData)
        """

        query = {"cmd": "getitemlist", "entityid": entityid, **params}

        r = self.get(urlencode(query))
        response = r.json()["response"]
        match response["code"]:
            case "OK":
                return response["items"]["item"]
            case "BadRequest":
                return f"BadRequest: {response['message']}"

        return r
