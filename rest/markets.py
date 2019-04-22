import requests
from utils.config import PATH, MARKET_ENDPOINTS
from utils.tools import  _check_endpoint, _check_errors, grab_headers

class Markets(object):
    def __init__(self):
        self._PATH = PATH
        self._class_type = "markets"
        
    def _get_all_markets(self) -> dict:
        _METHOD = "GET"
        _ENDPOINT = "/v1/markets"
        """
        :meth: _get_all_markets
        :args: None

        :returns:
        {
            "status": {
                "timestamp": "2018-06-02T22:51:28.209Z",
                "elapsed": 10
            },
            "data": [
            {
                "exchange": "binance",
                "base": "btc",
                "quote": "usdt",
                "pair": "btc-usdt"
                }
            ]
        }

        """
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=MARKET_ENDPOINTS)
        api_response = _request(url=self._PATH+_ENDPOINT, headers=grab_headers())
        return api_response.get_json()

        