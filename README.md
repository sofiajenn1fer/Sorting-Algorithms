# Python Sorting Algorithm Program

## Overview
This program allows users to input a list of numbers and choose from various sorting algorithms to sort the list. 
The program provides detailed step-by-step explanations of how the selected algorithm processes the list. Users can explore 
multiple sorting algorithms on the same array or input a new array to start over.

---

## Features
- Supports five sorting algorithms:
  1. Selection Sort
  2. Insertion Sort
  3. Bubble Sort
  4. Merge Sort
  5. Quick Sort
- Provides detailed, step-by-step explanations of the sorting process.
- Allows users to retry different sorting algorithms on the same input array.
- Offers the option to input a new array for sorting.

---

## File Description
**`main.py`**  
Contains the following:
1. **Sorting Functions**:
   - **`selection_sort`**:
     Performs selection sort, selecting the smallest element in each iteration and swapping it into place.
   - **`insertion_sort`**:
     Simulates the process of sorting a hand of cards by shifting elements and inserting them in the correct position.
   - **`bubble_sort`**:
     Compares adjacent elements and swaps them to "bubble" the largest elements to the end.
   - **`merge_sort`**:
     Recursively divides the array into halves, sorts, and merges them back.
   - **`quick_sort`**:
     Uses a pivot to partition the array into two parts and recursively sorts the partitions.

2. **Interactive Console Interface**:
   - Prompts the user for input (array of numbers).
   - Allows the user to choose a sorting algorithm and displays detailed steps and the final sorted list.
   - Enables retrying with different algorithms on the same array or starting with a new array.

---

## How to Run
1. Save the script as `main.py`.
2. Run the script in a Python 3.x environment:
   ```bash
   python main.py
