class Solution:
  def defangIPaddr(self, address: str) -> str:
    return address.replace(".", "[.]")

address = "127.0.0.1"
solution = Solution().defangIPaddr(address)

print(solution)
