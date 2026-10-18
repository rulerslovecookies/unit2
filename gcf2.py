def find_gcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x
num1 = int(input("give x: "))
num2 = int(input("give y: "))
gcf = find_gcf(num1, num2)
print(f"The GCF of {num1} and {num2} is: {gcf}")