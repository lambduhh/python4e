# Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below


fname = open("mbox-short.txt", "r")
fread = fname.readlines()

counts = dict()
for w in fread:
    if not w.startswith("From "): continue
    words = w.split()
    time = words[5]
    hour = time[:2]
    counts[hour] = counts.get(hour, 0) + 1
s = (sorted(counts.items()))

for k, v in s:
    print(k, v)

if __name__ == '__main__':
    print("Program being edited in a text editor")
