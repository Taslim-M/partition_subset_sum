# Pseudo-Polynomial Partition

This project provides a Python implementation of the partition problem, which divides a given list of integers into two subsets with equal sum. The algorithm is efficient enough to handle both positive and negative numbers, and it returns the indices of one subset. The remaining indices belong to the other subset.

## Problem Statement

Given a set of `n` integers `[a1, a2, …, an]`, the goal is to partition the list into two subsets so that the sums of the two subsets are equal. If the total sum of the set is `s = a1 + a2 + ... + an`, then the time complexity of the algorithm should ideally be `O(ns)`. This algorithm falls under the category of pseudo-polynomial algorithms due to the dependency on the term `s` in the time complexity.

## Features

- Handles both positive and negative integers in the input set.
- Returns the indices of one subset where the subset sum is equal to half of the total sum. False if it does not exist.
- Efficiently designed with a time complexity of `O(ns)`.

## Time Complexity

The time complexity of this algorithm is `O(ns)`, where `n` is the number of elements in the input list and `s` is the sum of the list elements. This complexity is achieved through a dynamic programming approach, making the algorithm efficient for large lists and suitable for cases where `s` is relatively small compared to `n`.

## Usage

- **Function**: `partition_helper` in `partition.py`
- **Input**: A list of integers (positive or negative).
- **Output**: Indices of one subset; remaining indices belong to the other subset.

### Example

```python
from partition import partition_helper

# Input list
arr = [1, 5, 11, 5]

# Get the partitioned subset indices
indices = partition_helper(arr)
print("Subset indices:", indices)
```

## Testing
Test cases for this project were generated using [chaotic_array_generator](https://github.com/btrindad/chaotic_array_generator) These test cases verify that the partition function correctly identifies subsets for a variety of input lists, including those with negative numbers.

## Requirements
Python: 3.x or later
