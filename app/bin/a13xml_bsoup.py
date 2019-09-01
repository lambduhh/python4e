import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_200770.xml'
xml = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(xml, 'lxml')
# after importing and interpreting the text using BS you are free to make inquires
s = soup.findAll('count')
numlist = list()
runtotal = 0

tags = soup('count')
for count in tags:
    numlist.append(int(count.contents[0]))

for val in numlist:
    runtotal = runtotal + val


if __name__ == '__main__':
    print('Count', len(numlist))
    print('Sum', runtotal)
