import requests
from utils.config import PATH, NEWS_ENDPOINTS
from utils.tools import  _check_endpoint, _check_errors, _check_optional_filter, grab_headers

class News(object):
    def __init__(self):
        self._PATH = PATH
        self._class_type = "news"

    def _get_all_news(self) -> dict:
        _METHOD = "GET"
        _ENDPOINT = "/v1/news"
        _REQUEST_FILTER = None #no filters available for this endpoint
        """
        :meth: _get_all_news
        :args: optional
        :optional args: `optional_filter`

        :returns:
        {
            "status": {
                "timestamp": "2018-06-02T22:51:28.209Z",
                "elapsed": 10
                },
            "data": [
                {
                "symbol": "btc",
                "name": "Bitcoin",
                "id": "1e31218a"
                }
            ]
        }

        """
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=NEWS_ENDPOINTS)
        if _REQUEST_FILTER is True:
            api_response = _request(url=self._PATH+_ENDPOINT+_REQUEST_FILTER, headers=grab_headers())
        else:
            api_response = _request(url=self._PATH+_ENDPOINT, headers=grab_headers())
        return api_response

    def _get_news_by_symbol(self, symbol: str) -> dict:
        """
        """
        _METHOD = "GET"
        _ENDPOINT = "v1/news/<symbol>/profile".replace("<symbol>", symbol)
        _REQUEST_FILTER = None #no filters available for this endpoint
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=NEWS_ENDPOINTS)
        api_response = _request(url=self._PATH+_ENDPOINT, headers=grab_headers())
        return api_response