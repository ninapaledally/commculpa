def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Please input a number: "))
print(is_even_or_odd(num))
