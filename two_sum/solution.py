class Solution:
  def solve(self, nums: [int], target: int) -> [int]:
    i, j = 0, 1
    while i < len(nums):
      while j < len(nums):
        if nums[i] + nums[j] == target:
          return [i, j]
        else:
          j += 1
      i += i
    return [0,0]
