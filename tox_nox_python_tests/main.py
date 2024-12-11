from calculator import add, subtract

def calculate():
    print(f"adding: 1+2 = {add(1, 2)}")
    print(f"subtracting: 5-3 = {subtract(5, 3)}")


if __name__ == '__main__':
    calculate()