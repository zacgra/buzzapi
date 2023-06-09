import requests
from urllib.parse import urljoin, urlencode
from dotenv import dotenv_values

from buzzapi.resources.get_user_activity_stream import GetUserActivityStream
from buzzapi.resources.get_entity_gradebook_2 import GetEntityGradebook2
from buzzapi.resources.get_enrollment_activity import GetEnrollmentActivity
from buzzapi.resources.get_enrollment_3 import GetEnrollment3
from buzzapi.resources.list_entity_enrollments import ListEntityEnrollments
from buzzapi.resources.get_item_list import GetItemList

env = dotenv_values(".env")


class Client(
    requests.Session,
    GetUserActivityStream,
    GetEntityGradebook2,
    GetEnrollmentActivity,
    GetEnrollment3,
    ListEntityEnrollments,
    GetItemList,
):
    """Client uses session to handle connections, token cookie, and persistent
    baseurl between requests.
    """

    def __init__(self, userspace_username: str, password: str) -> None:
        """Sets headers to JSON (rather than XML default), sets instance token,
        and baseurl.

        Args:
            userspace_username (str): same as Buzz API login credentials
            password (str): same as Buzz API login credentials
        """
        super().__init__()
        self.baseurl = "https://api.agilixbuzz.com/cmd"
        self.headers.update(
            {"Accept": "application/json", "Content-Type": "application/json"}
        )
        self.token = self.get_token(userspace_username, password)

    def request(
        self, method: str, url: str, *args, **kwargs
    ) -> requests.models.Response:
        """Overrides the Session.request method to inject the baseurl and
        token cookie in to each request.

        Args:
            method (str): HTTP request method string
            url (str): resource path string
        """

        # check prevents initial login3 request for token from failing before
        #   it has been set
        cookie = {}
        if hasattr(self, "token"):
            cookie = {"_token": self.token}

        return super().request(
            method, urljoin(self.baseurl, f"?{url}"), cookies=cookie, *args, **kwargs
        )

    def get_token(self, userspace_username: str, password: str) -> str:
        """Makes request using username/password to login3 and returns auth token

        Returns:
            str: token
        """
        query = {
            "cmd": "login3",
            "username": userspace_username,
            "password": password,
        }

        r = self.post(urlencode(query))
        response = r.json()

        token = ""
        if response["response"]["code"] == "OK":
            token = response["response"]["user"]["token"]

        return token


if __name__ == "__main__":
    client = Client(env["USERSPACE_USERNAME"], env["PASSWORD"])
