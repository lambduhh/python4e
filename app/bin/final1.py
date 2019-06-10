# Write a program that repeatedly prompts a user for integer numbers
#     until the user enters 'done'. Once 'done' is entered,
#     print out the largest and smallest of the numbers.
#     If the user enters anything other than a valid number catch it with a
#         try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

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


if __name__ == '__main__':

    alist = []

    while True:
        usrnumb = input("number please?")
        if usrnumb == 'done':
            break
        try:
            alist.append(float(usrnumb))
        except ValueError:
            print("try again :( ")

    sml = smaller(alist)
    lg = larger(alist)
    print("Minimum is ", sml)
    print("Maximum is ", lg)
