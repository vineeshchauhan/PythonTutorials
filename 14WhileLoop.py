i = 1

while i < 5:
    print(i)
    i+=1
i = 1
while i < 5:
    print('*'*i)
    i+=1

number = 9
guess = input('Enter your number ')
while int(guess) != number:
    guess = input('Enter your number ')
print('you won')