import random
import string
import csv
import progressbar


def getcount():
    rownums = int(input("How many email do you want?: "))
    try:
        rowint = int(rownums)
        return rowint
    except ValueError:
        print("Please enter an integer value")
        return getcount()


def makeEmail():
    extensions = ['com', 'net', 'org', 'gov']
    domains = [
        'gmail', 'yahoo', 'comcast', 'verizon', 'morocco', 'hotmail',
        'outlook', 'ma'
    ]

    winext = extensions[random.randint(0, len(extensions) - 1)]
    windom = domains[random.randint(0, len(domains) - 1)]

    acclen = random.randint(1, 20)

    winacc = ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(acclen))

    finale = winacc + "@" + windom + "." + winext
    return finale


#save count to var
howmany = getcount()

#counter for While loop
counter = 0

#empty array for loop
emailarray = []

#uses counter to figure out how many emails to keep making

print("Creating email addresses...")
print("Progress: ")

prebar = progressbar.ProgressBar(maxval=int(howmany))

for i in prebar(range(howmany)):
    while counter < howmany:
        emailarray.append(str(makeEmail()))
        counter = counter + 1
        prebar.update(i)

print("Creation completed.")

for i in emailarray:
    print(i)

