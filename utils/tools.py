from . import errors
import requests
from utils.config import ALLOWED_ASSET_FILTERS, ALLOWED_MARKET_FILTERS, ALLOWED_NEWS_FILTERS, API_VERSION
import os, platform

def _check_endpoint(method: str, endpoint: str, endpoint_dict: dict) -> requests:
    """
    """
    try:
        if endpoint in endpoint_dict:
            if method is endpoint_dict[endpoint][0]:
                return endpoint_dict[endpoint][1]
    except:
        raise BaseException(f"Invalid method:endpoint combination {method}:{endpoint}") 

def _check_optional_filter(class_type: str,  optional_filter: str) -> bool:
    """
    """
    class_to_filter = \
        {
            "assets": ALLOWED_ASSET_FILTERS,
            "market": ALLOWED_MARKET_FILTERS,
            "news": ALLOWED_NEWS_FILTERS,
        }
    try:
        if class_type in class_to_filter:
            if optional_filter in class_to_filter[class_type]:
                return True
        else:
            return False
    except:
        BaseException(f"Invalid optional_filter {optional_filter} for the given class_type {class_type}")
    
def grab_headers():
    headers = {}
    headers['User-Agent'] = 'messary-python/{} (Python {})'.format(
        API_VERSION,
        platform.python_version(),
    )
    headers['X-Messari-Client'] = 'python-{}'.format(API_VERSION)
    headers['Accept-Charset'] = 'utf-8'
    return headers