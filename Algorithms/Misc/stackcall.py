# stack call

def fact(x):
    if x == 1:           # Base case
        return 1
    else:                # Recursive case
        return x * fact(x-1)

print(fact(3))
