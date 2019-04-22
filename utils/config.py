import requests

"""
PATH
"""

PATH = "https://data.messari.io/api"

"""
API_VERSION
"""

API_VERSION = "1"

""" 
ENDPOINT: METHOD
"""

MARKET_ENDPOINTS = \
    {
        "/v1/markets": ["GET", requests.get]
    }

ASSET_ENDPOINTS = \
    {
        "/v1/assets": ["GET", requests.get],
        "/v1/assets/<symbol>/profile": ["GET", requests.get],
        "/v1/assets/<symbol>/metrics": ["GET", requests.get]
    }

NEWS_ENDPOINTS = \
    {
        "/v1/news": ["GET", requests.get],
        "/v1/news/<symbol>": ["GET", requests.get]
    }

""" 
ALLOWED FILTERS: Parse against this so we're not sending uneeded filter params to the server
"""

ALLOWED_MARKET_FILTERS = set(["with-metrics", "with-profiles", "with-metrics&with-profiles"])

ALLOWED_ASSET_FILTERS = set([])

ALLOWED_NEWS_FILTERS = set([])