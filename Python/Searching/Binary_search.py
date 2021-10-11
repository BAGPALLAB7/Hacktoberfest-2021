'''
Binary Search is one of the effective way of searching in a sorted array by splitting it into left and right halves.

Time Complexity : O(logn)
Space Complexity : O(1)
'''

def binary_search(elements, target):
    left_index = 0
    right_index = len(elements) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = elements[mid_index]

        if mid_number == target:
            return mid_index

        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    # Return -1 if no element is found
    return -1

if __name__ == '__main__':
    arr = [11,12,13,15,16,19,22]
    target = 12
    # Printing Binary Search
    print(binary_search(arr,target))
    # Output is 1
