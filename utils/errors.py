

class InvalidParam(Exception):
    """
    HTTP 400 Bad Request -> InvalidParam
    """
    pass

class Unauthorized(Exception):
    """
    HTTP 401 Bad Authentication -> Unauthroized
    """
    pass

class Forbidden(Exception):
    """
    Http 403 Forbidden -> Forbidden
    """
    pass

class RateLimit(Exception):
    """
    Http 429 Too Many Requests -> Rate Limited
    """
    pass

class UnexpectedError(Exception):
    """
    Http 500 Internal Server Error
    """ 