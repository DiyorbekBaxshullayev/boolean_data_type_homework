def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b = int(a)
    return a >= 0 and a == b

print(main(-2))