class Solution:
  def solve(self, encoded: [int], first: int) -> [int]:
    arr = [first]
    i = 0
    while i < len(encoded):
      arr.append(encoded[i] ^ arr[i])
      i += 1

    return arr
