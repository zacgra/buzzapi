from urllib.parse import urlencode
from typing import Optional


class GetUserActivityStream:
    def get_user_activity_stream(
        self, userid: int, enrollmentid: int, params: dict = {}
    ):
        activities = []
        response = self.get_user_activity_stream_limited(userid, enrollmentid, params)
        activity = response["activities"]["activity"]
        activities = activities + activity

        endkeyPresent = "endkey" in response["activities"]
        while endkeyPresent:
            startkey = response["activities"]["endkey"]
            response = self.get_user_activity_stream_limited(
                userid, enrollmentid, {"startkey": startkey, **params}
            )
            activity = response["activities"]["activity"]
            activities = activities + activity

            endkeyPresent = "endkey" in response["activities"]
            if endkeyPresent:
                startkey = response["activities"]["endkey"]

        return activities

    def get_user_activity_stream_limited(
        self, userid: int, enrollmentid: int, params: dict = {}
    ):
        query = {
            "cmd": "getuseractivitystream",
            "userid": userid,
            "enrollmentid": enrollmentid,
            "limit": 100,
            **params,
        }
        print(urlencode(query))
        r = self.get(urlencode(query))
        response = r.json()
        return response["response"]
