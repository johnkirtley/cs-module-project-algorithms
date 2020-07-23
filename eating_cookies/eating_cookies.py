import time

'''
Input: an integer
Returns: an integer
'''
start = time.time()


def eating_cookies(n, cache={}):

    # if n < 0:
    #     return 0

    # elif n < 1 or n == 1:
    #     return 1

    # else:
    #     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    if n < 0:
        return 0

    if n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-2, cache)
        return cache[n]


end = time.time()

print(f"Time taken was {end - start}")


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
