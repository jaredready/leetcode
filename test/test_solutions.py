import unittest
from remove_duplicates_from_sorted_array.solution import Solution as RemoveDuplicatesFromSortedArray
from number_of_good_pairs.solution import Solution as NumberOfGoodPairs
from defanging_an_ip_address.solution import Solution as DefangingAnIpAddress

class RemoveDuplicatesTestCase(unittest.TestCase):
  def test_solution(self):
    input = [0,0,1,1,1,2,2,3,3,4]
    expected = 5
    self.assertEqual(RemoveDuplicatesFromSortedArray().solve(input), expected)

class NumberOfGoodPairsTestCase(unittest.TestCase):
  def test_solution(self):
    input = [1,2,3,1,1,3]
    expected = 4
    self.assertEqual(NumberOfGoodPairs().solve(input), expected)

class DefangingAnIpAddressTestCase(unittest.TestCase):
  def test_solution(self):
    input = "127.0.0.1"
    expected = "127[.]0[.]0[.]1"
    self.assertEqual(DefangingAnIpAddress().solve(input), expected)

if __name__ == '__main__':
  unittest.main()
