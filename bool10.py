import math


def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b=math.sqrt(a)
    return a > 0 and int(b) ** 2 == a

print(main(16))
