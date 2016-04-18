"""Test for arrayflatten."""

import unittest

import arrayflatten

class TestArrayFlatten(unittest.TestCase):

  def test_nested_pass(self):
    testlist = [1, 2, 3, [4, 5], [6], []]
    expected = [1, 2, 3, 4, 5, 6]
    result = arrayflatten.nested(testlist)
    self.assertEqual(expected, result)

  def test_nested_fail(self):
    testlist = [1, 2, 3, [4, 5], [6], []]
    expected = [1, 2, 3, 4, 5]
    result = arrayflatten.nested(testlist)
    self.assertNotEqual(expected, result)

  def test_empty_target_pass(self):
    testlist = []
    expected = []
    result = arrayflatten.nested(testlist)
    self.assertEqual(expected, result)

  def test_nested_empty_target_pass(self):
    testlist = [[], [[]]]
    expected = []
    result = arrayflatten.nested(testlist)
    self.assertEqual(expected, result)

  def test_bad_target_raise(self):
    with self.assertRaises(TypeError):
      arrayflatten(['', None])


if __name__ == '__main__':
  unittest.main()
