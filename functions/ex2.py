# non parameterized function

# create
def armstrong():
    num = input('enter a number')     # bad practice
    if num.isnumeric():
        power = len(num) # stores the num of digits
        num = int(num)   # convert num into integer
        total = 0      
        temp = num
        while temp > 0:
            r = temp % 10
            total += r ** power
            temp //= 10
        if num == total:
            print('armstrong')
        else:
            print('not armstrong')
    else:
        print('invalid input')

# call
armstrong()
armstrong()
armstrong()


