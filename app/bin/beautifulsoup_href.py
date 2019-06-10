import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 7
position = 18

# Retrieve all of the anchor tags
url = 'http://py4e-data.dr-chuck.net/known_by_Rebbecca.html'


def fetch(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return list(tags)


def follow(link, count):
    if count == 0:
        return link
    links = fetch(link)
    return follow(links[17].attrs['href'], count - 1)


if __name__ == '__main__':
    print(follow(url, count))
