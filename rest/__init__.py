class Client(object):
    """
    Messari client for accessing api attributes
    """
    def __init__(self):
        self._assets = None 
        self._markets = None
        self._news = None


    @property
    def assets(self):
        """
        """
        if self._assets is None:
            from assets import Assets
            self._assets = Assets(self)
        return self._assets

    @property
    def markets(self):
        """
        """
        if self._markets is None:
            from markets import Markets
            self._markets = Markets(self)
        return self._markets

    @property
    def news(self):
        """
        """
        if self._news is None:
            from news import News
            self._news = News(self)
        return self._news