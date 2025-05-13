def is_prime(num):
    is_prime = False
    if num == 2:
        is_prime = True
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
    return is_prime