class Fruit:

    def __init__(self,name, taste,color,shape,size):
        self.name = name
        self.taste = taste
        self.color = color
        self.shape = shape
        self.size = size

    def show(self):
        print("fruit details")
        print(f'name={self.name}')
        print(f'shape={self.shape}')
        print(f'color={self.color}')
        print(f'size={self.size}')
        print(f'taste={self.taste}')
        
    def make_ripe(self,new_color):
        self.color = new_color

class Melon(Fruit):

    # override
    def __init__(self,name,size,color,taste,shape,region):
        super().__init__(name,taste,color,shape,size) # super class constructor also updated
        self.region = region  # added a new property to Melon

    def sell_melon(self,price):
        print(f'sold {self.name} for {price}')
    
    def purchase_melon(self,price):
        print(f'purchased {self.name} for {price}')
    
    # override
    def show(self):
        super().show()
        print(f'found in region={self.region}')

print(dir(Melon))
m1 = Melon('watermelon','big','dark-green','sweet','sperical','Rajasthan')   
m1.show() 
m1.purchase_melon(200)
