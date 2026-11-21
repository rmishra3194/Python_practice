#exercise 1
import math
def mysqrt(a):
    """Estimates the square root of a using Newton's method."""
    x = a / 2.0  # Initial estimate (any positive value works, e.g., 1 or a/2)
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y


def test_square_root():
    """Prints a comparison table of mysqrt vs math.sqrt for numbers 1 to 9."""
    # Print table headers
    print(f"{'a':<4} {'mysqrt(a)':<18} {'math.sqrt(a)':<18} {'diff'}")
    print(f"{'-':<4} {'---------':<18} {'------------':<18} {'----'}")

    for a in range(1, 10):
        my_val = mysqrt(a)
        math_val = math.sqrt(a)
        diff = abs(my_val - math_val)
        # Format columns to align neatly regardless of decimal length
        print(f"{float(a):<4.1f} {my_val:<18} {math_val:<18} {diff}")

#print(mysqrt(10))

def print_n(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff!")


def sequence(n):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


def eval_loop():
    while True:
        line = input('> ')
        if line == ('done'):
            break
        else:
            print(eval(line))

#eval_loop()

def estimate_pi():
    """Estimates the value of pi using srinivasa ramanujan's formula."""
    total = 0
    k = 0
    while True:
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = math.factorial(k) ** 4 * (396 ** (4 * k))
        one_term = numerator / denominator
        total += one_term
        k += 1

        if one_term < 1e-15: 
            break
    total *= (2 * math.sqrt(2)) / 9801
    return 1/total

#print(estimate_pi(), math.pi)


        

