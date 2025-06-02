name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 17<age<60: 
    print('Welcome to working life '+ name)
else : 
    if age < 18:
        print('Stay at home kiddo')

    else:
        print('Time to retire Grampa '+ name)