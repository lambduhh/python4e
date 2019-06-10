# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:


import urllib.request, json

with urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_200771.json") as url:
    data = json.loads(url.read().decode())

    numlist = []

    for item in data['comments']:
        countnum = int(item['count'])
        addtolist = numlist.append(countnum)
        s = sum(numlist)
        print(s)
