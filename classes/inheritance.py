class Material:
    def __init__(self,name):
        self.name = name

    def calculate_volume(self, h,w,l):
        return h * w * l

class MetalMaterial(Material):
    pass


m1 = Material('wood')
m2 = MetalMaterial('steel')

vol = m1.calculate_volume(100,20,400)    
print(m1.name,vol)

vol2 = m2.calculate_volume(120,50,100)
print(m2.name, vol2)