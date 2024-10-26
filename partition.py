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
    
    return dp[len(arr)][target_sum]



arr = [1, 1, 4, 5, 9]
print(partition(arr))