number = 9
turns = [1,2,3,4,5]

for num in turns:

    guess= int(input("Please enter your guess: "))

    if guess==number:
        print("Well Done")
        break

    else:
        if guess> number:
            print("please guess lower")
            
        else:
            print("please guess higher")


if guess ==number:
    print('You win')
    
else:
    print('Game Over')