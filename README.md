# buzzapi

An API client for the Agilix/Buzz LMS API

## Overview

The Agilix Buzz API is RESTful API for the Buzz LMS that accepts XML by default,
but can also accept and serve JSON. It consists of both paginated un-paginated
data, and requires a login token cookie for almost every endpoint.

The `buzzapi` package handles storing the login token as a cookie to be passed
with each request, as well as pagination on the relevant endpoints.

## Setup

See `.env_example` for the necessary environment variables. These need to be
set in the `.env` file located in the root directory.

```py
# Create a new Client with a Session and the login token set
client = Client(
    config["USERSPACE_USERNAME"],
    config["PASSWORD"],
)

#
```
