# *args
# variable number of arguments can be passed 
def avg(*numbers):
    if numbers:
        return sum(numbers)/len(numbers)

def guestlist(*guestname):
    print("these are the guest for the event")
    for name in guestname:
        print('!!!',name,'!!!')


if __name__ == "__main__":
    a = avg(12,4,23,2,32,1,76,21,45,89,23)
    b = avg()
    c = avg(12,34,45)
    print(a)
    guestlist('raju','shaka','rohan','dev','devi')
