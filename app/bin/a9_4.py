# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# *The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail.
# *The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = open("mbox-short.txt", "r")
fread = fname.readlines()

counts = dict()
for w in fread:
    if not w.startswith("From:"): continue
    words = w.split()
    emails = words[1]
    counts[emails] = counts.get(emails, 0) + 1

bigwerd = None
bigcount = None
for k, v in counts.items():
    if bigcount is None or v > bigcount:
        bigwerd = k
        bigcount = v
if __name__ == '__main__':
    print(bigwerd, bigcount)
