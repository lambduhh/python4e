import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if __name__ == '__main__':
    url = 'http://py4e-data.dr-chuck.net/comments_200768.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # after importing and interpreting the text using BS you are free to make inquires
    s = soup.findAll('span')
    numlist = list()
    runtotal = 0

    tags = soup('span')
    for tag in tags:
        numlist.append(int(tag.contents[0]))

    for val in numlist:
        runtotal = runtotal + val

        print('Count', len(numlist))
        print('Sum', runtotal)
