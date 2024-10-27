from partition import partition_helper

import json

# Specify the path to your JSON file
file_path = 'test_cases.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    test_cases = json.load(file)

for i, test_case in enumerate(test_cases, 1):
    arr = test_case['Array']
    result = partition_helper(arr)
    partition = [arr[i] for i in result]
    function_result = sum(partition)
    if function_result == test_case['Sum']:
        print(f"Test case {i}: PASS")
    else:
        print(f"Test case {i}: FAIL (Expected: {test_case['Sum']}, Got: {function_result})")