from urllib.parse import urlencode


class GetEnrollment3:
    def get_enrollment_3(self, enrollmentid: int):
        """This command gets enrollment data for a particular enrollment.

        Args:
            enrollmentid (int): ID of the enrollment to get.
            select: 	Comma-separated list of which data to return.
                        By default, GetEnrollment3 returns only the enrollment node.
                        See https://api.agilixbuzz.com/docs/#!/Command/GetEnrollment3
        """

        query = {
            "cmd": "getenrollment3",
            "enrollmentid": enrollmentid,
        }
        r = self.get(urlencode(query))
        response = r.json()["response"]

        if response["code"]:
            return response["enrollment"]
