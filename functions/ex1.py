def greet():
    print('welcome to Wakanda')

def greetMore():
    print('*' * 20)
    print('Hi there')
    print('*' * 20)

def greetPerson(name):
    greet()
    print(name,"You are not welcome here")


greet()
greetMore()

greetPerson("Alex")
greetPerson("Raj")
greetPerson(200)

greetPerson() # error

