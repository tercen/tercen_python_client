from urllib.error import HTTPError

import pytson as ptson
import urllib.request
import io

from tercen.base.BaseObject import BaseObject

from tercen.model.base import *


class TercenError(Exception):
    pass


class HttpClientService:
    def __init__(self):
        super().__init__()
        self.tercenClient = None

    def getHttpClient(self):
        return self.tercenClient.httpClient

    def getBaseUri(self, uri):
        pass

    def getServiceUri(self, uri):
        return self.tercenClient.tercenURI.resolve(uri)

    def onResponseError(self, response):
        data = response.body().bytes()
        try:
            obj = decodeTSON(data)
            raise TercenError(str(obj))
        except BaseException:
            raise TercenError('unknown : failed to decode')

    def onError(self, error):
        raise error
        # raise TercenError() from error
        # pass

    def fromJson(self, m, useFactory=True):
        pass

    def specificClassFromJson( self, m):
        className = m['kind']
                
        klass = globals()[className]
        newObj = klass(m)

        return newObj

    def get(self, str_id, useFactory=True):
        try:
            params = {"id": str_id, "useFactory": str(useFactory).lower()}
            url = self.getServiceUri(self.getBaseUri()).replaceQueryParameters(params)
            response = self.tercenClient.httpClient.get(url.uri)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                # return self.fromJson(decodeTSON(response.body().bytes()))
                return self.specificClassFromJson(decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)

    def create(self, obj: BaseObject):
        try:
            response = self.getHttpClient().put(
                self.getServiceUri(self.getBaseUri()).toString(), None, encodeTSON(obj.toJson()))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                return self.fromJson(decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)

    def update(self, obj: BaseObject):
        try:
            response = self.getHttpClient().post(
                self.getServiceUri(self.getBaseUri()).toString(), None, encodeTSON(obj.toJson()))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                obj.rev = decodeTSON(response.body().bytes())[0]
        except BaseException as e:
            self.onError(e)

    def delete(self, obj_id: str, rev: str):
        try:
            params = {"id": obj_id, "rev": rev}
            url = self.getServiceUri(self.getBaseUri()).replaceQueryParameters(params)
            response = self.tercenClient.httpClient.delete(url.uri, None)
            if response.code() != 200:
                self.onResponseError(response)
        except BaseException as e:
            self.onError(e)

# self.findKeys("findByOwner", keys, useFactory)

    def findKeys(self, view_name, keys, useFactory=False):
        try:
            params = {'useFactory': str(useFactory).lower()}
            url = self.getServiceUri(self.getBaseUri()).resolve(URI.create(view_name)).replaceQueryParameters(params)
            response = self.getHttpClient().post(url.toString(), None, encodeTSON(keys))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                return list(map(lambda x: self.specificClassFromJson(x), decodeTSON(response.body().bytes())))
        except BaseException as e:
            self.onError(e)

    def findStartKeys(self, view_name, startKey, endKey, limit=20, skip=0, descending=True, useFactory=False):
        try:
            params = {'useFactory': str(useFactory).lower()}
            url = self.getServiceUri(self.getBaseUri()).resolve(URI.create(view_name)).replaceQueryParameters(params)
            response = self.getHttpClient().post(url.toString(), None, encodeTSON({
                'startKey': startKey,
                'endKey': endKey,
                'limit': limit,
                'skip': skip,
                'descending': descending
            }))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                return list(map(lambda x: self.specificClassFromJson(x), decodeTSON(response.body().bytes())))
        except BaseException as e:
            self.onError(e)


class URI:
    def __init__(self, base_url, path=None, args_dict=None):
        super().__init__()
        url_parts = list(urllib.parse.urlparse(base_url))
        if path is not None:
            url_parts[2] = path
        if args_dict is not None:
            url_parts[4] = urllib.parse.urlencode(args_dict)
        self.uri = urllib.parse.urlunparse(url_parts)

    def toString(self):
        return self.uri

    def replaceQueryParameters(self, args_dict):
        url_parts = list(urllib.parse.urlparse(self.uri))
        url_parts[4] = urllib.parse.urlencode(args_dict)
        return URI(urllib.parse.urlunparse(url_parts))

    def resolve(self, uri):
        if self.uri.endswith('/'):
            return URI(self.uri + uri.uri)
        else:
            return URI(self.uri + '/' + uri.uri)

    @classmethod
    def create(cls, param):
        return URI(param)


class HttpClient:
    def __init__(self):
        self.authorization = None

    def buildHeaders(self, headers):
        if headers is None:
            if self.authorization is None:
                return dict()
            else:
                headers = dict()
                headers["authorization"] = self.authorization
                return headers
        else:
            if self.authorization is None:
                return headers
            else:
                headers["authorization"] = self.authorization
                return headers

    def get(self, uri, headers={}):
        try:
            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), method='GET')
            return Response(urllib.request.urlopen(req))
        except HTTPError as e:
            return Response(e)

    def post(self, uri, headers, body):
        try:
            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), data=body, method='POST')
            return Response(urllib.request.urlopen(req))
        except HTTPError as e:
            return Response(e)

    def put(self, uri, headers, body):
        try:
            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), data=body, method='PUT')
            return Response(urllib.request.urlopen(req))
        except HTTPError as e:
            return Response(e)

    def delete(self, uri, headers):
        try:
            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), data=None, method='DELETE')
            return Response(urllib.request.urlopen(req))
        except HTTPError as e:
            return Response(e)


    def multipart(self, uri, headers=None, parts=None):
        if parts is None:
            parts = []
        if headers is None:
            headers = {}
        try:
            frontier = "ab63a1363ab349aa8627be56b0479de2"
            data = MultiPartMixTransformer(frontier, parts).encode_parts()
            headers["Content-Type"] = "multipart/mixed; boundary=" + frontier
            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), data=data, method='POST')
            return Response(urllib.request.urlopen(req))
        except HTTPError as e:
            return Response(e)


class Response:
    def __init__(self, httpResponseOrError):
        if httpResponseOrError is HTTPError:
            self.status = httpResponseOrError.code
            self.data = httpResponseOrError.read()
        else:
            self.status = httpResponseOrError.status
            self.data = httpResponseOrError.read()

    def code(self):
        return self.status

    def body(self):
        return Body(self.data)


class Body:
    def __init__(self, bytes_data):
        self.data = bytes_data

    def bytes(self):
        return self.data


class MultiPart:
    def __init__(self, headers, bytes_data):
        self.headers = headers
        self.bytes_data = bytes_data


class MultiPartMixTransformer:
    def __init__(self, frontier, parts):
        self.frontier = frontier
        self.parts = parts

    def encode_parts(self):
        data = bytearray()
        for part in self.parts:
            data.extend("--".encode("utf-8"))
            data.extend(self.frontier.encode("utf-8"))
            data.extend([13, 10])

            for key, value in part.headers.items():
                data.extend(key.encode("utf-8"))
                data.extend(": ".encode("utf-8"))
                data.extend(value.encode("utf-8"))
                data.extend([13, 10])

            data.extend([13, 10])
            data.extend(part.bytes_data)
            data.extend([13, 10])

        data.extend("--".encode("utf-8"))
        data.extend(self.frontier.encode("utf-8"))
        data.extend("--".encode("utf-8"))
        data.extend([13, 10])

        return data


def encodeTSON(obj):
    # tson_bytes = ptson.encodeTSON(obj)
    # tson_bytes.seek(0)
    # encObj = tson_bytes.read()
    return ptson.encodeTSON(obj).getbuffer().tobytes()


def decodeTSON(bytes):
    iobytes = io.BytesIO()
    iobytes.write(bytes)
    iobytes.seek(0)
    # decodedTson = ptson.decodeTSON(iobytes)
    return ptson.decodeTSON(iobytes)
