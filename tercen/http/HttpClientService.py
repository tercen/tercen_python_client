from urllib.error import HTTPError

#import sys  
#sys.path.append("./src/pytson")

import pytson as ptson
import urllib.request


from tercen.base.BaseObject import BaseObject

from tercen.model.impl import *


#import tercen.util.pytmp as ptmp


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
        # data = response.body().bytes()
        # data = response.stream.read()
        try:
            obj = decodeTSON(response)
            raise TercenError(str(obj))
        except BaseException:
            raise TercenError('unknown : failed to decode')

    def onError(self, error):
        raise error
        # raise TercenError() from error
        # pass

    def fromJson(self, m, useFactory=True):
        pass

    def get(self, str_id, useFactory=True):
        try:
            params = {"id": str_id, "useFactory": str(useFactory).lower()}
            url = self.getServiceUri(self.getBaseUri()).replaceQueryParameters(params)
            response = self.tercenClient.httpClient.get(url.uri)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                return self.fromJson(decodeTSON(response))
                # return self.specificClassFromJson(decodeTSON(response))
        except BaseException as e:
            self.onError(e)

    def create(self, obj: BaseObject):
        try:
            response = self.getHttpClient().put(
                self.getServiceUri(self.getBaseUri()).toString(), None, encodeTSON(obj.toJson()))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                return self.fromJson(decodeTSON(response))
        except BaseException as e:
            self.onError(e)

    def update(self, obj: BaseObject):
        try:
            response = self.getHttpClient().post(
                self.getServiceUri(self.getBaseUri()).toString(), None, encodeTSON(obj.toJson()))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                obj.rev = decodeTSON(response)[0]
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


    def findKeys(self, view_name, keys, useFactory=False):
        try:
            params = {'useFactory': str(useFactory).lower()}
            url = self.getServiceUri(self.getBaseUri()).resolve(URI.create(view_name)).replaceQueryParameters(params)
            response = self.getHttpClient().post(url.toString(), None, encodeTSON(keys))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                # return list(map(lambda x: self.specificClassFromJson(x), decodeTSON(response)))
                return list(map(lambda x: self.fromJson(x), decodeTSON(response)))
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
                # return list(map(lambda x: self.specificClassFromJson(x), decodeTSON(response)))
                return list(map(lambda x: self.fromJson(x), decodeTSON(response)))
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
            # data = MultiPartMixTransformer(frontier, parts).encode_parts()
            data = MultiPartMixTransformer(frontier, parts) # TODO Add json serializer iterator to this
            headers["Content-Type"] = "multipart/mixed; boundary=" + frontier

            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), data=data, method='POST')

            return Response(urllib.request.urlopen(req))

        except HTTPError as e:
            return Response(e)

    def multipart_non_chunked(self, uri, headers=None, parts=None):
        if parts is None:
            parts = []
        if headers is None:
            headers = {}
        try:
            frontier = "ab63a1363ab349aa8627be56b0479de2"
            data = MultiPartMixTransformerNonChunked(frontier, parts).encode_parts()
            headers["Content-Type"] = "multipart/mixed; boundary=" + frontier
            req = urllib.request.Request(uri, headers=self.buildHeaders(headers), data=data, method='POST')

            return Response(urllib.request.urlopen(req))

        except HTTPError as e:
            return Response(e)


class Response:
    def __init__(self, httpResponseOrError):
        # if httpResponseOrError is HTTPError:
        #     self.status = httpResponseOrError.code
        #     self.data = httpResponseOrError.read()
        # else:
        self.status = httpResponseOrError.status
        self.stream = httpResponseOrError


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

    def toTson(self):
        return {"headers":self.headers, "content":self.bytes_data}

class MultiPartMixTransformerNonChunked:
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

class MultiPartMixTransformer:
    def __init__(self, frontier, parts):
        self.frontier = frontier
        self.parts = parts
        # self.data = self.encode_parts(parts)
        self.jsonIter = None
        self.doneIter = False
        self.currentPart = 0
    
    def init_encode(self, part):
        data = bytearray()
        data.extend("--".encode("utf-8"))
        data.extend(self.frontier.encode("utf-8"))
        data.extend([13, 10])

        for key, value in part.headers.items():
            data.extend(key.encode("utf-8"))
            data.extend(": ".encode("utf-8"))

            data.extend(value.encode("utf-8"))
            data.extend([13, 10])

        data.extend([13, 10])

        return data

    def finish_encode(self):
        data = bytearray()
        
        data.extend([13, 10])

        return data

    def finish_all_encode(self):
        data = bytearray()
        data.extend("--".encode("utf-8"))
        data.extend(self.frontier.encode("utf-8"))
        data.extend("--".encode("utf-8"))
        
        data.extend([13, 10])
        return data


    def encode_part(self,part):
        data = bytearray()
        

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

       
        return data


    def __iter__(self):
        return self

    def __next__(self):
        if self.currentPart >= len(self.parts) or self.doneIter:
            if not self.doneIter:
                self.doneIter = True
                return self.finish_all_encode()
            else:
                raise StopIteration
        elif isinstance(self.parts[self.currentPart].bytes_data, bytes):
            self.currentPart = self.currentPart + 1
            return self.encode_part(self.parts[self.currentPart-1])
        elif isinstance(self.parts[self.currentPart].bytes_data, dict):
            if self.jsonIter is None:
                #FIXME change here to ptson
                self.jsonIter = ptson.SerializerJsonIterator(self.parts[self.currentPart].bytes_data)
                return self.init_encode(self.parts[self.currentPart])

            try:
                return self.jsonIter.__next__()
            except StopIteration:
                self.currentPart = self.currentPart  + 1
                return self.finish_encode()
        
 


#FIXME Has to be a request object!
def encodeTSON(obj ):
    # tson_bytes = ptson.encodeTSON(obj)
    # tson_bytes.seek(0)
    # encObj = tson_bytes.read()

    # return ptson.encodeTSON(obj).getbuffer().tobytes()
    return ptson.encodeTSON(obj).getbuffer().tobytes()


def decodeTSON(bts : Response):
    # iobytes = io.BytesIO()
    # iobytes.write(bts)
    # iobytes.seek(0)
    # decodedTson = ptson.decodeTSON(iobytes)
    return ptson.decodeTSON(bts.stream)
