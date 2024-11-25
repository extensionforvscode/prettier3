def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        half = n//2
        a = x//(10**half)
        b = x%(10**half)
        c = y//(10**half)
        d = y%(10**half)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a+b, c+d) - ac - bd

        return ac*(10**(2*half)) + ad_bc*(10**(half)) + bd
    
if __name__ == "__main__":
    # x = int(input("Enter first number:- "))
    # y = int(input("Enter second number:- "))
    # result = karatsuba(x, y)
    # print(f"Karatsuba({x}, {y}) = {result}")

    multiplication = input("Enter the multiplication :- ").strip()
    x, y = multiplication.split("x")
    result = karatsuba(int(x), int(y))
    print(f"{multiplication} = {result}")