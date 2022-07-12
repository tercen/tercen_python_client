import tercen.client.factory_base
from tercen.http.HttpClientService import URI


class TercenClient(tercen.client.factory_base.TercenClientBase):
    def __init__(self, uri=None):
        super().__init__()
        if uri is None:
            self.tercenURI = URI.create("https://tercen.com/")
        else:
            self.tercenURI = URI.create(uri)
