import httplib
import urlparse

TIMEOUT = 60

BUFFER_SIZE = 4096

def application(environ, start_response):
    request_uri = environ["REQUEST_URI"]
    url = "http://" + request_uri[1:]
    o = urlparse.urlparse(url)
    if not o.hostname:
        start_response("200 OK", [])
        yield "Hello"
    else:
        request_method = environ["REQUEST_METHOD"]
        request_headers = [(k[5:].replace("_", "-").title(), v) for k, v in environ.iteritems()
                           if k.startswith("HTTP_") and not k.startswith("HTTP_X_") and k != "HTTP_HOST"]
        request_headers.append(("Host", o.hostname))
        content_type = environ["CONTENT_TYPE"]
        if content_type:
            request_headers.append(("Content-Type", content_type))
        content_length = environ["CONTENT_LENGTH"]
        post_data = environ["wsgi.input"].read(int(content_length)) if content_length else None
        kwargs = {"port": o.port} if o.port else dict()
        conn = httplib.HTTPConnection(o.hostname, timeout=TIMEOUT, **kwargs)
        conn.request(request_method, url, body=post_data, headers=dict(request_headers))
        r = conn.getresponse()
        status = "%d %s" % (r.status, r.reason)
        response_headers = r.getheaders()
        start_response(status, response_headers)

        data = "1"
        while data:
            data = r.read(BUFFER_SIZE)
            yield data
