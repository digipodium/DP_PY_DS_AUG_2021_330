class Dog:
    # class variables
    age = 0
    color = 'brown'
    breed = 'german shepard'
    eyecolor = 'black'
    height = 10
    weight = 10
    kind = 'pet'

    # instance method
    def bark(self):
        print('bow wow '* 3)

    def eat(self,food):
        print(f'dog eats {food}')

class Goat:
    # class variables
    age = 0
    color = 'black'
    height = 10

    # instance method
    def eat_leaves(self):
        print('the goat eats some leaves')


moti = Dog()
tiger = Dog()

moti.bark()
tiger.bark()

moti.breed = "hybrid"
moti.age = 5
moti.color = 'black and white'
print("moti details=>",moti.age ,moti.breed ,moti.color)

tiger.age = 2
tiger.color = 'golden brown'
tiger.breed = 'Golden retreiver'
print("tiger details=>",tiger.age, tiger.breed, tiger.color)

malti = Goat()
malti.eat_leaves()
