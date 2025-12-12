"""
A helper to calculate prime numbers.
"""


def divisors_exist(target, prime_numbers):
    """
    Returns true if there is at least one prime number in the list
    which divides +target+
    """
    for prime_number in prime_numbers:
        if target % prime_number == 0:
            return True
    return False


def resolve_all_prime_numbers(target, prime_numbers):
    """
    A very primitive, naive prime calculator: calculates
    all primes up until +target+. It is not optimized because
    not many prime numbers are needed anyways.
    """
    last_known_prime_number = prime_numbers[-1]
    if target <= last_known_prime_number:
        return

    for prime_number_candidate in range(last_known_prime_number + 1, target + 1):
        if not divisors_exist(prime_number_candidate, prime_numbers):
            prime_numbers.append(prime_number_candidate)

def resolve_prime_numbers(target, prime_numbers) -> list[int]:
    """
    Resolves the prime numbers of +target+
    """
    resolve_all_prime_numbers(target, prime_numbers)
    return [prime_number
            for prime_number in prime_numbers
            if target % prime_number == 0]


if __name__ == "__main__":
    prime_numbers = [2]
    resolve_all_prime_numbers(100, prime_numbers)
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print("The primes up til 100 are calculated correctly:",
          prime_numbers == expected_primes)
    print("the primes of 22222 are correct:",
          resolve_prime_numbers(22222, prime_numbers) == [2, 41, 271])
