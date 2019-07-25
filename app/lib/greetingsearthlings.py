def smaller(l):
    mint = l[0]
    for a in l:
        if a < mint:
            mint = a
    return mint


def larger(l):
    maxx = l[0]
    for p in l:
        if p > maxx:
            maxx = p
    return maxx



def openbyline(file):
    fname = open(file, "r")
    fread = fname.readlines()
    return fread


def openfilelist(file):
    fname = open(file, "r")
    fread = fname.read()
    pieces = fread.split()
    return pieces
