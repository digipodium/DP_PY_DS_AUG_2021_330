
# required parameter 
def adder(a,b,c):
    return a+b+c

# default parameter
def multiplier(a,b,c=2):
    return a * b * c

def divisor(a,b=1,c=1):
    return a / b / c

# all default
def pythagoras(perpendicular=None,base=None):
    if perpendicular and base:
        hyp = (perpendicular ** 2 + base ** 2) ** .5
        return hyp


if __name__ == "__main__":
    divisor(5,4,2)

    # named arguments call
    divisor(a=5,b=4,c=2)
    divisor(10,c=5,b=2)

    print(pythagoras())
    print(pythagoras(perpendicular=4,base=3))