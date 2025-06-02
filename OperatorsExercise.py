name = input('Please enter you name: ')
age = int(input('Please enter your age: '))
if 17<age<31:
    print('Welcome to the holiday package ' + name)
else:
    if age < 18:
        print('Sorry, you are too young for the holiday package... You can try our other package! ' + name)
    else:
        print('Sorry, you are too old for the holiday package... You can try our other package! ' + name) 