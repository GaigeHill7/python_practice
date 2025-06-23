print("Welcome to my Computer Quiz :)")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0

print("Awesome thanks for playing :)")

#Question 1
answer = input ("What does CPU stand for: ")
if answer.lower() == 'central processing unit':
        print('Correct')
        score +=1
else:
      print('Incorrect')

#Question 2
answer = input ("What does BIOS stand for: ")
if answer.lower() == 'basic input output system':
        print('Correct')
        score +=1
else:
      print('Incorrect')

#Question 3
answer = input ("What does DHCP stand for: ")
if answer.lower() == 'dynamic host configuration protocol':
        print('Correct')
        score+=1
else:
      print('Incorrect')

#Question 4
answer = input ("What does FTP stand for: ")
if answer.lower() == 'file transfer protocol':
        print('Correct')
        score+=1
else:
      print('Incorrect')

#Results
print('You scored '+ str(score) + ' points')