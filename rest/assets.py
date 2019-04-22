import requests
from utils.config import PATH, ASSET_ENDPOINTS
from utils.tools import  _check_endpoint, _check_errors, _check_optional_filter, grab_headers

class Assets(object):
    def __init__(self):
        self._PATH = PATH
        self._class_type = "assets"

    def _get_all_assets(self, optional_filter="") -> dict:
        """
        """
        _METHOD = "GET"
        _ENDPOINT = "/v1/assets"
        _REQUEST_FILTER = _check_optional_filter(class_type=self._class_type, optional_filter=optional_filter)
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=ASSET_ENDPOINTS)
        if _REQUEST_FILTER is True:
            api_response = _request(url=self._PATH+_ENDPOINT+_REQUEST_FILTER, headers=grab_headers())
        else:
            api_response = _request(url=self._PATH+_ENDPOINT, headers=grab_headers())
        return api_response.get_json()

    def _get_only_asset_symbols(self) -> dict:
        """
        """
        _METHOD = "GET"
        _ENDPOINT = "/v1/assets"
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=ASSET_ENDPOINTS)
        api_response = _request(url=self._PATH+_ENDPOINT)
        symbols = [value["symbol"] for value in api_response["data"] if "data" in api_response]
        return symbols

    def _get_asset_profile_by_symbol(self, symbol: str) -> dict:
        """
        """
        _METHOD = "GET"
        _ENDPOINT = "v1/assets/<symbol>/profile".replace("<symbol>", symbol)
        _REQUEST_FILTER = None #no filters available for this endpoint
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=ASSET_ENDPOINTS)
        api_response = _request(url=self._PATH+_ENDPOINT, headers=grab_headers())
        return api_response.get_json()

    def _get_asset_metrics_by_symbol(self, symbol: str) -> dict:
        """
        """
        _METHOD = "GET"
        _ENDPOINT = "v1/assets/<symbol>/metrics".replace("<symbol>", symbol)
        _REQUEST_FILTER = None #no filters available for this endpoint
        _request = _check_endpoint(method=_METHOD, endpoint=_ENDPOINT, endpoint_dict=ASSET_ENDPOINTS)
        api_response = _request(url=self._PATH+_ENDPOINT, headers=grab_headers())
        return api_response.get_json()
