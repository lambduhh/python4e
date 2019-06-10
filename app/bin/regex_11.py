# #The basic outline of this problem is to read the file, look for
# integers using the re.findall(), looking for a regular expression of '[0-9]+' and
# then converting the extracted strings to integers and summing up the integers.

import re

if __name__ == '__main__':
    fname = open("regex.data.txt", "r")
    fread = fname.readlines()
    su = 0
    for l in fread:
        words = l.split()
        for num in words:
            m = re.findall('[0-9]+', num)
            if m:
                for n in m:
                    n = int(n)
                    su = n + su
    print(su)
