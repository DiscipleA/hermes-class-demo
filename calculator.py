def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Return a / b, or None when b is zero (including floating signed zero)."""
    if b == 0:
        return None
    return a / b


def main(x=10, y=0):
    """Print the demo result, explaining zero division without a traceback."""
    print("Simple Calculator Demo")
    result = divide(x, y)
    if result is None:
        print(f"{x} / {y} = undefined (division by zero)")
    else:
        print(f"{x} / {y} = {result}")


if __name__ == "__main__":
    main()
