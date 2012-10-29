import webapp2
from google.appengine.api import urlfetch

def opm_fetch(request, url):
    result = urlfetch.fetch(url="http://" + url,
                        payload=request.body,
                        method=request.method,
                        headers=request.headers,
                        deadline=60)
    response = webapp2.Response()
    response.status = result.status_code
    response.headers = result.headers
    response.body = result.content
    return response

app = webapp2.WSGIApplication([("/([^/]+)", opm_fetch)])