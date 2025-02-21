import math


def f(y, z, x):
    numerator = (78 * x**2 + y**3 + 35)**7 - (abs(z)**4) / 16
    denominator = (47 * (y - z**3 - 81)**3 +
                   47 * (math.floor(89 - x**3))**4)
    first_part = numerator / denominator

    second_part_numerator = (math.atan(x) -
                             33 * (33 * y**3 - 1 - 49 * z)**3)
    second_part_denominator = (math.sin(z)**5 -
                               math.tan(74 * y**3 + 42 * x**2 + 1)**4)
    second_part = second_part_numerator / second_part_denominator

    return first_part - second_part


if __name__ == '__main__':
    test_cases = [
        (-0.06, -0.1, -0.07),
        (-0.36, 1.0, 0.29),
        (0.9, -0.99, 0.13),
        (0.59, -0.9, 0.8),
        (-0.08, -0.94, 0.1),
    ]

    for case in test_cases:
        result = f(*case)
        print(f"f{case} = {result:.2e}")