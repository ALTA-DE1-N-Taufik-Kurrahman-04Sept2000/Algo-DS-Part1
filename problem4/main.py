def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_grid(width, height, start):
    result = ""
    current_number = start
    while is_prime(current_number):
        current_number += 1
    for row in range(height):
        row_values = []
        for col in range(width):
            while not is_prime(current_number):
                current_number += 1
            row_values.append(current_number)
            current_number += 1
        result += " ".join(map(str, row_values)) + "\n"
    return result
if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """