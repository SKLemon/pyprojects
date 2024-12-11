#Created as a part of the BAIL repository on Github. Created 12/05/2024


def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range (2,num):
        if num % i == 0:
            return False
    return True

prime_check = int(input(("Type your number here: ")))
print(is_prime(prime_check))
