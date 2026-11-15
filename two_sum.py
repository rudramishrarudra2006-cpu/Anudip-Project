def two_sum(nums, target):
    """
    Finds indices of two numbers that add up to the target.
    Time Complexity: O(n) | Space Complexity: O(n)
    """
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []


if __name__ == "__main__":
    sample_nums = [2, 7, 11, 15]
    target_val = 9
    print("Indices:", two_sum(sample_nums, target_val))
