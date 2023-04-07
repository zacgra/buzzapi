from urllib.parse import urlencode


class ListEntityEnrollments:
    def list_entity_enrollments(self, entityid: int):
        """This command gets enrollment data for a particular enrollment.

        Args:
            entityid (int): ID of the course or group for which to get the enrollment list.
            params (dict): Additional args as dict
                           ex: {'userid': 12345}
        """

        query = {
            "cmd": "listentityenrollments",
            "entityid": entityid,
        }
        r = self.get(urlencode(query))
        response = r.json()["response"]

        if response["code"]:
            return response["enrollments"]["enrollment"]
