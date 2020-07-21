import random

def roll_a_dice():
    num = random.randint(1,6)
    return num

def main():
    dice_list = []
    TRIALS = 100
    for i in range(TRIALS):
        dice_num = roll_a_dice()
        dice_list.append(dice_num)
        print(dice_list)
        print("You have rolled a {}".format(dice_num))  

    ave = sum(dice_list) / TRIALS

    print("The average number rolled is {}".format(ave))

main()