def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Intentional flaw: No check for b == 0
    return a / b

if __name__ == "__main__":
    print("Simple Calculator Demo")
    x = 10
    y = 0
    
    # Intentional flaw: Will crash when executed
    print(f"{x} / {y} = {divide(x, y)}")
