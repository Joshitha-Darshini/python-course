import random #imprting module
playing = True #initialise
number = str(random.randint(10,20))
#random in-built function
print("i will  generate a number from 0 tp 9, and you have to guess the number one digut at a time.")
print("the game ends when you get 1 hero!")
#iterate loop till the condition is true 
while playing:
    guess= input("give me your best guess!\n")
    if number == guess:

        print("ypu win the game")
        print("the number was",number)
        break
    else:
        print("yor guess isn't quite right,try again.\n")
    