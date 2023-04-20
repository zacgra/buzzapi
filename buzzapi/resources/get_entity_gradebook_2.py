from urllib.parse import urlencode
from typing import List


class GetEntityGradebook2:
    def get_entity_gradebook_2(self, entityid: int, params: dict = {}) -> List[dict]:
        """Gets grades for all students enrolled in specified entity.
        The entity id can be a Course ID, Section ID, or Group ID.

        Args:
            entityid (int): Course ID, Section ID, or Group ID
            params (dict): Additional args as dict
                           ex: {'itemid': 12345 }
        Returns:
            dict: List of enrollments un
        """
        query = {
            "cmd": "getentitygradebook2",
            "entityid": entityid,
            **params,
        }

        r = self.get(urlencode(query))
        if r:
            response = r.json()["response"]
            match response["code"]:
                case "OK":
                    return response["enrollments"]["enrollment"]
                case "BadRequest":
                    return f"BadRequest: {response['message']}"

        return r
