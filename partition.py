# Backtracking to find the subset indices
def backtrack(arr, dp, target_sum):
    subset_indices = []
    i, j = len(arr), target_sum
    
    while i > 0 and j > 0:
        # Check if this element was included in the subset
        if dp[i][j] and not dp[i - 1][j]:
            subset_indices.append(i - 1)  
            j -= arr[i - 1]  # Reduce the remaining sum by the element's value
        i -= 1  # Move to the previous row

    subset_indices.reverse()  # Reverse to get the indices in the correct order
    return subset_indices

def partition(arr):
    total_sum = sum(arr)
    # If the total sum is odd, two equal subsets is not possible
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    # Initialize a 2D list to store the boolean values
    dp = [[False] * (target_sum + 1) for _ in range(len(arr) + 1)]
    # print(T)
    
    # Populate the first column with True as we can always form a sum of 0 with an empty subset
    for i in range(len(arr) + 1):
        dp[i][0] = True
    
    # fill DP Table
    for i in range(1, len(arr) + 1):
        for j in range(1, target_sum + 1):
            if j - arr[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    if not dp[len(arr)][target_sum]:
        return False

    # if exist, return indices
    subset_indices = backtrack(arr, dp, target_sum)
    return subset_indices

def partition_helper(arr):
    # print(arr)
    min_val = min(arr)
    if min_val < 0:
        arr = [x + abs(min_val) + 1 for x in arr]
    # print(arr)
    return partition(arr)

def main():
    #arr = [1, 1, 4, 5, 9]
    arr = [5, -1, 3, 1]
    result = partition_helper(arr)
    if result:
        print("Subset:", [arr[i] for i in result])
    else:
        print("Subset does not exist")


main()