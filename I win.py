odd = 1
while (odd < 300):
    print odd
    odd = odd + 2

import random
rand = random.randint (0,50)
daInput = raw_input()
while (rand != daInput):
    if (rand < daInput):
        print "too high!"
    elif (rand > daInput):
        print "too low!"
if (rand == daInput):
    print "you win!"
    