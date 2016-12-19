import random
def guess_number():
    min = raw_input("Enter the mininum number on the dice : ")
    int_min = int(min)
    max = raw_input("Enter the max number on the dice : ")
    int_max = int(max)
    while (int_min < int_max):
        random_num = random.randint(int_min, int_max)
        print random_num
        int_min = int_min + 1
    print("done")

roll_dice()
