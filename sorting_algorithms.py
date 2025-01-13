# Selection sort function
def selection_sort(arr):
    # storing each step
    steps = []
    for i in range(len(arr)):
        # setting minimum index to current index
        minimum = i
        # traversing through array from i
        for j in range(i + 1, len(arr)):
            # checking if current element is less than minimum, if so it becomes minimum
            if arr[j] < arr[minimum]:
                minimum = j
        # swap
        arr[i], arr[minimum] = arr[minimum], arr[i]
        steps.append(f"Step {i + 1}: Swapped {arr[minimum]} with {arr[i]} -> {arr}")
    return steps


# Insertion sort function
def insertion_sort(arr):
    # storing each step
    steps = []
    # traversing through array skipping first element
    for i in range(1, len(arr)):
        # storing current index
        key = arr[i]
        # storing index before current index
        j = i - 1
        # checking if j is in bounds and while current index is less than j
        while j >= 0 and key < arr[j]:
            # swap neighboring elements
            arr[j + 1] = arr[j]
            steps.append(f"Moved {arr[j]} to position {j + 1}")
            # decrement j
            j -= 1
        # final swap with "initial" index
        arr[j + 1] = key
        steps.append(f"Inserted {key} at position {j + 1} -> {arr}")
    return steps


# Bubble sort function
def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(f"Swapped {arr[j]} with {arr[j + 1]} -> {arr}")
    return steps


# Merge sort function
def merge_sort(arr):
    # storing each step
    steps = []

    # helper function to merge array
    def merge(left, right):
        result = []

        # sorting both lists
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # combining results (sorted list) and returning
        result.extend(left or right)
        return result

    # dividing array and merging
    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        merged = merge(left, right)
        steps.append(f"Merged {left + right} -> {merged}")
        return merged

    sorted_arr = divide(arr)
    steps.append(f"Final sorted list: {sorted_arr}")
    arr[:] = sorted_arr
    return steps


# Quicksort function
def quick_sort(arr):
    # storing steps
    steps = []

    #helper function to identify pivot point for swapping
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            # if current index is less than or equal to pivot value
            if arr[j] <= pivot:
                i += 1
                # swap elements
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(f"Swapped {arr[i]} with {arr[j]} -> {arr}")
        # change position of pivot value
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(f"Moved pivot {pivot} to position {i + 1} -> {arr}")
        return i + 1

    # recursive helper for sorting
    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(arr) - 1)
    return steps

def main():
    input_vals = ["yes", "Yes", "y", "Y", ""]
    end = ""
    while end in input_vals:
        print("\nEnter a list of numbers separated by spaces:")
        user_input = input()
        original = list(map(int, user_input.split()))
        repeat = ""

        while repeat in input_vals:
            print("\nChoose a sorting method:")
            print("1. Selection Sort")
            print("2. Insertion Sort")
            print("3. Bubble Sort")
            print("4. Merge Sort")
            print("5. Quick Sort")
            
            choice = int(input("\nEnter your choice (1-5): "))

            arr = original.copy()  

            if choice == 1:
                steps = selection_sort(arr)
            elif choice == 2:
                steps = insertion_sort(arr)
            elif choice == 3:
                steps = bubble_sort(arr)
            elif choice == 4:
                steps = merge_sort(arr)
            elif choice == 5:
                steps = quick_sort(arr)
            else:
                print("Invalid choice!")
                return
            
            print(f"\nOriginal array: {original}")

            print("\nDetailed steps:")
            for step in steps:
                print(step)
            print(f"\nSorted list: {arr}")

            repeat = str(input("\nWould you like to try with a different sorting algorithm? "))

        end = str(input("\nWould you like to input a new array for sorting? "))

if __name__ == "__main__":
    main()