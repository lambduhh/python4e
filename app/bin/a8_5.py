# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

from app.lib.greetingsearthlings import openbyline

fname = open("mbox-short.txt", "r")
fread = fname.readlines()
count = 0
for w in fread:
    if not w.startswith("From:"): continue
    count = count + 1
    words = w.split("@")
if __name__ == '__main__':
    print(words[1])
