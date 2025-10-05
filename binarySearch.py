def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    # Take user input for the array
    arr = list(map(int, input("Enter sorted elements separated by spaces: ").split()))

    # Take input for the element to search
    target = int(input("Enter the element to search: "))

    # Perform binary search
    result = binary_search(arr, target)

    # Display result
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array.")


# Entry point of the program
if __name__ == "__main__":
    main()

