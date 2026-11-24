"""
Experiment No. 10 (CO-4)
Apply NumPy to create a one-dimensional array containing the numbers from 1 to 10,
perform slicing operations, compute statistical measures (sum, mean, maximum, and
minimum), and apply broadcasting to modify the array elements.
"""

import numpy as np


def main() -> None:
    # 1. Create a 1D NumPy array containing numbers from 1 to 10
    arr = np.arange(1, 11)
    print("Original 1D Array:", arr)
    print("-" * 55)

    # 2. Perform slicing operations
    print("Slicing Operations:")
    print(f"  First 5 elements (arr[:5])       : {arr[:5]}")
    print(f"  Last 3 elements (arr[-3:])       : {arr[-3:]}")
    print(f"  Middle slice (arr[3:7])          : {arr[3:7]}")
    print(f"  Alternate elements (arr[::2])    : {arr[::2]}")
    print(f"  Reversed array (arr[::-1])       : {arr[::-1]}")
    print("-" * 55)

    # 3. Compute statistical measures
    total_sum = np.sum(arr)
    mean_val = np.mean(arr)
    max_val = np.max(arr)
    min_val = np.min(arr)

    print("Statistical Measures:")
    print(f"  Sum     : {total_sum}")
    print(f"  Mean    : {mean_val:.2f}")
    print(f"  Maximum : {max_val}")
    print(f"  Minimum : {min_val}")
    print("-" * 55)

    # 4. Apply broadcasting to modify array elements
    added_arr = arr + 10
    multiplied_arr = arr * 5
    print("Broadcasting Operations:")
    print(f"  Add 10 to all elements (arr + 10)      : {added_arr}")
    print(f"  Multiply all elements by 5 (arr * 5)   : {multiplied_arr}")


if __name__ == "__main__":
    main()
