class Solution:
  def solve(self, nums: [int]) -> int:
    appearances = {}
    for num in nums:
      if not num in appearances:
        appearances[num] = 1
      else:
        appearances[num] += 1

    goodPairs = 0
    for appearance in appearances:
      goodPairs += appearances[appearance] * (appearances[appearance] - 1) // 2

    return goodPairs
