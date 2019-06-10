# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see
# if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

if __name__ == '__main__':

    def tryingthisout(words, res):
        if len(words) == 0:
            return res
        elif words[0] not in res:
            res = [words[0], *res]  # iterable unpacking aka [words[0]] + res
            words = words[1:]
            return tryingthisout(words, res)
        else:
            words = words[1:]
            return tryingthisout(words, res)


    fname = open("romeo.txt", "r")
    fread = fname.read()
    emptylist = []
    pieces = fread.split()

    t = tryingthisout(pieces, emptylist)
    s = sorted(t)
    print(s)
