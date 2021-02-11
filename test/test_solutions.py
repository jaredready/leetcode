import unittest
from remove_duplicates_from_sorted_array.solution import Solution as RemoveDuplicatesFromSortedArray
from number_of_good_pairs.solution import Solution as NumberOfGoodPairs
from defanging_an_ip_address.solution import Solution as DefangingAnIpAddress
from decode_xored_array.solution import Solution as DecodeXORedArray
from sum_of_all_odd_length_arrays.solution import Solution as SumOfAllOddLengthArrays

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

class DecodeXORedArrayTestCase(unittest.TestCase):
  def test_solution(self):
    inputEncoded = [1,2,3]
    inputFirst = 1
    expected = [1,0,2,1]
    self.assertEqual(DecodeXORedArray().solve(inputEncoded, inputFirst), expected)

class SumOfAllOddLengthArraysTestCase(unittest.TestCase):
  def test_solution(self):
    input = [1,4,2,5,3]
    expected = 58
    self.assertEqual(SumOfAllOddLengthArrays().solve(input), expected)
    
if __name__ == '__main__':
  unittest.main()
