from typing import TypedDict, Any


class HttpResponse(TypedDict):
    statusCode: int
    body: Any


class ServerError(Exception):
    def __init__(self):
        super().__init__("Internal server error")


def bad_request(error: Exception) -> HttpResponse:
    return {"statusCode": 400, "body": error}


def server_error() -> HttpResponse:
    return {"statusCode": 500, "body": ServerError()}


def created() -> HttpResponse:
    return {"statusCode": 201, "body": None}


def ok(data: Any) -> HttpResponse:
    return {"statusCode": 200, "body": data}
