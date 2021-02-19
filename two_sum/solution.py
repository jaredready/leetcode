class Solution:
  def solve(self, nums: [int], target: int) -> [int]:
    map = dict(zip(nums, range(0, len(nums))))
    for i, num in enumerate(nums):
      complement = target - num
      if complement in map and map[complement] != i:
        return [i, map[complement]]
    
    return [0,0]
