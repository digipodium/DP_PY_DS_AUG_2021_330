class Rectangle:

    def __init__(self,h, w):
        self.height = h
        self.width = w

    def area(self):
        return self.height * self.width

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        return False

    def __repr__(self) -> str:
        return f'Rec h:{self.height},w:{self.width}'

# usage
item1 = Rectangle(100,100)
item2 = Rectangle(105,10)
item3 = Rectangle(3,50)

# if item1.area() > item2.area() and item1.area() > item3.area():
#     print(f'item 1 is bigger')
# elif item2.area() > item1.area() and item2.area() > item3.area():
#     print(f'item 2 is bigger')
# else:
#     print(f'item 3 is bigger')

if item1 > item2 and item1 > item3:
    print('item1 is bigger')
elif item2 > item1 and item2 > item3:
    print('item2 is bigger')
else:
    print('item3 is bigger')

item4 = Rectangle(5,50)
item5 = Rectangle(51,50)

x = [item1,item2,item3,item4,item5]
x.sort()
print(x)