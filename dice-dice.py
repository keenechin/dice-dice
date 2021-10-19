import numpy as np

N=100000
results = []

def upgrade(dice):
    dice = dice +2
    if dice > 12:
        dice = 20
    return dice

def roll(dice, running=0):
    a = np.random.randint(dice) + 1
    b = np.random.randint(dice) + 1
    total = np.abs(a-b) + running
    if a == b:
        if a == 1:
            return 1
        dice = upgrade(dice)
        additional = roll(dice, total)
        total = total + a + additional
    return total

import sys
for i in range(N):
    result = roll(int(sys.argv[1]))
    results.append(result)

running=0
average = 0
last_per = 0
cumlist = []
perlist = []
for i in range(1, np.max(results)):
    percentage=np.around(results.count(i)/N, 4)
    running=running+last_per
    average += i*percentage
    last_per = percentage
    cumlist.append(running)
    perlist.append(percentage)


for i in range(1, 12):
    percentage = perlist[i]
    running = cumlist[i]
    print((i,np.around( percentage*100,3), np.around(100*(1- running), 3) ))
print(f"Average result: {average}")
