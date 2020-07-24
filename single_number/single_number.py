import time
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
start = time.time()


def single_number(arr):
    count = {}

    for i in range(len(arr)):
        current = arr[i]

        if current not in count:
            count[current] = 1
        else:
            count[current] += 1

    for key, value in count.items():
        if value == 1:
            return key

    # s = set()

    # for x in arr:
    #     if x in s:
    #         s.remove(x)
    #     else:
    #         s.add(x)

    # return list(s)[0]


end = time.time()

print(f"Time taken was {end - start}.")


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
