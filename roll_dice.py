import random

total = 0
TRIALS = 100
for i in range(TRIALS):
    dice_num = random.randint(1, 6)
    print("You have rolled a {}".format(dice_num))
    total += dice_num

ave = total / TRIALS

print("The average number rolled is {}".format(ave))
