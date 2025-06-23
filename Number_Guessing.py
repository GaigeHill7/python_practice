import random

top_of_range = input('Give a number ')

# Check if input is number and above 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print('Please type a number larger than 0')
        quit()
else:
    print('Type a number')
    quit()


#Establishing a random number in range
num = random.randrange(top_of_range)


for i in range(3):
    guess = input('Guess a number: ')
    guess = int(guess)

    if guess == num:
        print("Awesome, you are good at this.")
        quit()
    else:
        up_or_below = guess - num
        print(f'nope, try again. You have {2-i} tries left.')
        
        #Above or below number
        if up_or_below > 0:
            print('Your guess is bigger than the number')
        else:
            print('Your number is smaller than the number')

print(f'Sorry, the number was {num}')




