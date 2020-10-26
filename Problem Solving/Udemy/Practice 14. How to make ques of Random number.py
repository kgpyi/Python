from random import randint

rand_num = randint(1, 1000)
trial_num = 1
user_num = 0
while user_num != rand_num:
    print("Trail Number is: ", trial_num)
    user_num = int(input("Enter your guess : "))

    if user_num > rand_num:
        print("Your number is greater, try again: ")
    elif user_num < rand_num:
        print("Your number is less, try again: ")
    elif user_num == rand_num:
        print("Your gussed it, may you have a good day")
        break
    trial_num += 1

