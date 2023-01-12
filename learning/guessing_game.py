
low = 1
high = 1000
guesses = 1
print("think of a number between 1 to 1000 ")
user_input = int(input("enter the number : "))
while True:
    guess = low+(high-low)//2
    msg_var = """my guess is {}, Should i guess higher or lower, 
    Press h if higher 
    press l if lower or press c if it is a correct guess. 
    """
    system_input = input(msg_var.format(guess))
    if system_input == "h":
        low = guess+1
    elif system_input == "l":
        high = guess-1
    elif system_input == "c":
        print("i got it in {} guesses".format(guesses))
        break
    guesses += 1
