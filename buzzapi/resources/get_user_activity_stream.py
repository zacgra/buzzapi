from urllib.parse import urlencode
from typing import Optional


class GetUserActivityStream:
    def get_user_activity_stream(
        self, userid: int, enrollmentid: int, params: dict = {}
    ) -> list:
        all_activities = []
        activities = self.get_user_activity_stream_limited(userid, enrollmentid, params)
        if activities:
            all_activities = all_activities + activities["activity"]

        endkeyPresent = "endkey" in activities
        while endkeyPresent:
            startkey = activities["endkey"]
            activities = self.get_user_activity_stream_limited(
                userid, enrollmentid, {"startkey": startkey, **params}
            )

            if activities:
                all_activities = all_activities + activities["activity"]

            endkeyPresent = "endkey" in activities
            if endkeyPresent:
                startkey = activities["endkey"]

        return all_activities

    def get_user_activity_stream_limited(
        self, userid: int, enrollmentid: int, params: dict = {}
    ) -> dict:
        query = {
            "cmd": "getuseractivitystream",
            "userid": userid,
            "enrollmentid": enrollmentid,
            "limit": 100,
            **params,
        }
        print(urlencode(query))
        r = self.get(urlencode(query))
        if r.ok:
            return r.json()["response"]["activities"]

        raise Exception("Error: Unable to retrieve resource", r)
