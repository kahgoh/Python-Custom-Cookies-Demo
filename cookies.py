from cookielib import Cookie
from cookielib import CookieJar
from urllib2 import Request
import urllib2
import urllib

'''
    Makes a cookie with provided name and value.
'''
def makeCookie(name, value):
    return Cookie(
        version=0, 
        name=name, 
        value=value,
        port=None, 
        port_specified=False,
        domain="kahdev.bur.st", 
        domain_specified=True, 
        domain_initial_dot=False,
        path="/", 
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )

# Making use of the cookies:
jar = CookieJar()

request = Request(url="http://kahdev.bur.st/python/cookies/receiver.php")

jar.set_cookie(makeCookie("name", "kahdev"))
jar.set_cookie(makeCookie("where", "here"))
#jar.add_cookie_header(request)

# Now, let us try open and read.
opener = urllib2.build_opener()
request.add_header("Cookie", "something=test+1+2+3; source=script")
f = opener.open(request)

print "Server responds with: "
print f.read()
