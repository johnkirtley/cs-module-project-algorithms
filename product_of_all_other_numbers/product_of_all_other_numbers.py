from functools import reduce
import time
'''
Input: a List of integers
Returns: a List of integers
'''

start = time.time()


def product_of_all_other_numbers(arr):

    newArr = []

    for i in range(len(arr)):
        temp = arr[:i]+arr[i+1:]
        result = reduce(lambda a, b: a * b, temp)
        newArr.append(result)

    return newArr

    # placeholder = [0] * len(arr)

    # for i in range(len(arr)):
    #     newArr = arr.copy()
    #     newArr[i] = 1
    #     result = 1

    #     for value in newArr:
    #         result = result * value
    #         placeholder[i] = result

    # return placeholder


end = time.time()

print(f"Time taken was {end - start}.")


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
