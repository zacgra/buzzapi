# from urllib.parse import urlencode
# from typing import Optional


# class GetEnrollment3:
#     def get_enrollment_3(self, enrollmentid: int, select: Optional[list] = None):
#         """This command gets enrollment data for a particular enrollment.

#         Args:
#             enrollmentid (int): ID of the enrollment to get.
#             select: 	Comma-separated list of which data to return.
#                         By default, GetEnrollment3 returns only the enrollment node.
#                         See https://api.agilixbuzz.com/docs/#!/Command/GetEnrollment3
#         """

#         query = {
#             "cmd": "getenrollment3",
#             "enrollmentid": enrollmentid,
#             "select": select,
#         }
#         r = self.get(urlencode(query))
#         response = r.json()["response"]

#         if response["code"]:
#             return response


# class GetEnrollmentActivity:
#     def get_enrollment_activity(self, enrollmentid: int, params: dict = {}) -> list:
#         """This command gets the activity detail for the specified user enrollment.

#         Args:
#             enrollmentid (int): Enrollment ID of user for which to get activity.
#             params (dict): Additional args as dict
#                            ex: {'startdate': "2022-08-18T16:06:51.747Z" }

#         Returns:
#             list: List of enrollment activities
#         """

#         query = {
#             "cmd": "getenrollmentactivity",
#             "enrollmentid": enrollmentid,
#             **params,
#         }
#         r = self.get(urlencode(query))
#         response = r.json()["response"]

#         if response["code"]:
#             return response["enrollment"]["activity"]


# class GetEntityGradebook2:
#     def get_entity_gradebook_2(self, entityid: int, params: Optional[dict] = {}):
#         """Gets grades for all students enrolled in specified entity.
#         The entity id can be a Course ID, Section ID, or Group ID.

#         Args:
#             entityid (int): Course ID, Section ID, or Group ID
#             params (dict): Additional args as dict
#                            ex: {'itemid': 12345 }
#         Returns:
#             dict: List of enrollments un
#         """
#         query = {
#             "cmd": "getentitygradebook2",
#             "entityid": entityid,
#             **params,
#         }

#         return self.get(urlencode(query))


# class GetUserActivityStream:
#     def get_user_activity_stream(self, userid: int, enrollmentid: int):
#         activities = []
#         response = self.get_user_activity_stream_limited(userid, enrollmentid, {})
#         activity = response["activities"]["activity"]
#         activities = activities + activity

#         endkeyPresent = "endkey" in response["activities"]
#         while endkeyPresent:
#             startkey = response["activities"]["endkey"]
#             response = self.get_user_activity_stream_limited(
#                 userid, enrollmentid, {"startkey": startkey}
#             )

#             activity = response["activities"]["activity"]
#             activities = activities + activity

#             endkeyPresent = "endkey" in response["activities"]
#             if endkeyPresent:
#                 startkey = response["activities"]["endkey"]

#         return activities

#     def get_user_activity_stream_limited(
#         self, userid: int, enrollmentid: int, params: Optional[dict] = {}
#     ):
#         query = {
#             "cmd": "getuseractivitystream",
#             "userid": userid,
#             "enrollmentid": enrollmentid,
#             "limit": 100,
#             **params,
#         }
#         r = self.get(urlencode(query))
#         response = r.json()
#         return response["response"]
