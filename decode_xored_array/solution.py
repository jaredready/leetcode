from itertools import accumulate
from operator import xor

class Solution:
  def solve(self, encoded: [int], first: int) -> [int]:
    return list(accumulate([first] + encoded, xor))
