def removeDuplicates(nums: [int]) -> int:
  '''
  This implementation keeps two pointers, i and j, where i the slow walker and j is the fast walker.
  As long as nums[i] == nums[j] then we're in a series of duplicates. Once nums[i] != nums[j]
  we know we ended the duplicate series and we copy nums[j] onto nums[i + 1] and increment i.
  This has the effect of "shifting" the unique elements down the array until j == len(nums).
  We return i as it is the last unique element of the array. The consumer can slice the array at i
  to return an array of just unique elements.

  Complexity
  O(n) time  - i and j traverse at most once through the input
  O(1) space - no additional space over the input is required
  '''
  if len(nums) <= 0:
    return 0
  
  i, j = 0, 1
  while j < len(nums):
    if nums[i] != nums[j]:
      nums[i + 1] = nums[j]
      i += 1
    else:
      j += 1

  return i + 1

input = [1,1,2,3,4,5,5,5,6,7,8,9,9,9,9]

answer = removeDuplicates(input)
print(answer)
print(input[:answer])