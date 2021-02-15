# Modified "Regrouping the Sum" from https://web.stanford.edu/class/cs9/sample_probs/SubarraySums.pdf
class Solution:
  def solve(self, arr: [int]) -> int:
    n = len(arr)
    return sum(((n - i) * (i + 1) + (n % 2)) // 2 * a for i, a in enumerate(arr))
