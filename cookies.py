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

# Create a cookie jar to store our custom cookies.
jar = CookieJar()

# Generate a request to make use of these cookies.
request = Request(url="http://kahdev.bur.st/python/cookies/receiver.php")

# Use makeCookie to generate a cookie and add it to the cookie jar.
jar.set_cookie(makeCookie("name", "kahdev"))
jar.set_cookie(makeCookie("where", "here"))

# Add the cookies from the jar to the request.
jar.add_cookie_header(request)

# Now, let us try open and read.
opener = urllib2.build_opener()
f = opener.open(request)

print "Server responds with: "
print f.read()
