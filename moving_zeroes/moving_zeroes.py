import time
'''
Input: a List of integers
Returns: a List of integers
'''

start = time.time()


def moving_zeroes(arr):
    # Your code here

    for i in range(len(arr)):
        if arr[i] == 0:
            arr.remove(arr[i])
            arr.append(0)
    return arr

    # return [notZero for notZero in arr if notZero != 0] + [zero for zero in arr if zero == 0]


end = time.time()

print(f"Time was {end - start}.")


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
