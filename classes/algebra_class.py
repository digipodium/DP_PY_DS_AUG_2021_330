
class Algebra:

    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def linear_equation_1(self):
        return self.x ** 2 + self.y ** 2 + self.x * self.y * 2
    
    def linear_equation_2(self):
        return self.x ** 2 + self.y ** 2 - self.x * self.y * 2

    def quad_eq_1(self,z):
        pass


f = Algebra(2,3)
print(f.linear_equation_1())
print(f.linear_equation_2())
g = Algebra(12,23)
print(g.linear_equation_1())
print(g.linear_equation_2())