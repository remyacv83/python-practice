import random
def guess_number():
    random_num = random.randint(1 , 10)
    user_input = int(raw_input("Gues a number between 1 and 10"))
    if( random_num == user_input):
        print("You guessed it right")
        break;
     elif(random_num > user_input):
         print("The number you entered is less than the correct number");
         user_input = int(raw_input("Try again by entering a number greater than "+user_input))
         break;
     elif(random_num < user_input):
        print("The number you entered is greater than the correct number");
         user_input = int(raw_input("Try again by entering a number less than "+user_input))
         break;
    print("done")

guess_number()
