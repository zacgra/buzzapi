from urllib.parse import urlencode


class GetEnrollmentActivity:
    def get_enrollment_activity(self, enrollmentid: int, params: dict) -> list:
        """This command gets the activity detail for the specified user enrollment.

        Args:
            enrollmentid (int): Enrollment ID of user for which to get activity.
            params (dict): Additional args as dict
                           ex: {'startdate': "2022-08-18T16:06:51.747Z" }

        Returns:
            list: List of enrollment activities
        """

        query = {
            "cmd": "getenrollmentactivity",
            "enrollmentid": enrollmentid,
            **params,
        }
        r = self.get(urlencode(query))
        response = r.json()["response"]

        match response["code"]:
            case "OK":
                return response["enrollment"]["activity"]
            case _:
                return response
