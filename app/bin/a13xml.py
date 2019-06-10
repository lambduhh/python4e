import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_200770.xml'
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
print(tree)
counts = tree.findall('.//count')
# c = counts[0].find('count').text
print(counts)

