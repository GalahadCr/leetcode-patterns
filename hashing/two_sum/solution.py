from typing import List


def two_sum(self, nums: List[int], target: int) -> List[int]:
    """
    Finds two indices such that their values add up to the target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int]: Indices of the two numbers.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    raise ValueError("No valid solution found")
