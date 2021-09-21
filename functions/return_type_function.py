def add_3():
    x = input("X:")
    y = input("Y:")
    z = input("Z:")
    tot = int(x) + int(y) + int(z)
    return tot

# using a value returning function
add_3()  # the answer will not be display and it will be lost 👎

ans = add_3() # the answer will not be display but stored in ans variable
print(ans)    # the variable can be used in code later ✔

print(add_3()) # the answer will be display but not stored in any variable ✔

output = add_3() + add_3() - add_3() # return type functions can be used in expression also ✔
print(output)