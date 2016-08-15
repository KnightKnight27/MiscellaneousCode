from __future__ import division
import nextnum
import unittest


class TestRandomGenBoundaryConditions(unittest.TestCase):
    """
    Set of unit-tests for the RandomGen class, focussing on
    checking corner-case behaviour.
    """
    def test_throws_if_negative_probabilities_used(self):
        test_values = [1]
        test_probabilities = [-0.1]

        with self.assertRaises(StandardError):
            generator = nextnum.RandomGen(test_values, test_probabilities)

    def test_throws_if_probabilities_do_not_sum_to_one(self):
        test_values = [1, 2]
        test_probabilities = [0.4, 0.59]

        with self.assertRaises(StandardError):
            generator = nextnum.RandomGen(test_values, test_probabilities)

    def test_throws_if_input_lists_are_different_lengths(self):
        test_values = [1, 2, 3]
        test_probabilities = [0.2, 0.2]

        with self.assertRaises(StandardError):
            generator = nextnum.RandomGen(test_values, test_probabilities)


class TestCumulativeSum(unittest.TestCase):
    """
    Set of unit-tests for the cumulative_sum function
    """
    def test_only_returns_values_in_input_values_list(self):
        test_values = [1, 2, 3, 4, 5]
        results = nextnum.cumulative_sum(test_values)
        self.assert_(results == [1, 3, 6, 10, 15])


class TestFindLeftmostValueGreaterThanX(unittest.TestCase):
    def test_throws_if_given_empty_list(self):
        test_values = []
        test_value = 0.0

        with self.assertRaises(StandardError):
            return_value = nextnum.find_index_of_leftmost_value_greater_than_x(
                               test_values,
                               test_value
                           )

    def test_throws_if_test_value_larger_than_highest_value_in_list(self):
        test_values = [0.0, 1.0]
        test_value = 2.0

        with self.assertRaises(StandardError):
            return_value = nextnum.find_index_of_leftmost_value_greater_than_x(
                               test_values,
                               test_value
                           )

    def test_returns_index_of_lowest_value_if_test_value_is_lower(self):
        test_values = [0.0, 1.0]
        test_value = -1.0

        return_value = nextnum.find_index_of_leftmost_value_greater_than_x(
                            test_values,
                            test_value
                       )

        self.assert_(return_value == 0)


class TestNextNum(unittest.TestCase):
    """
    Set of unit-tests for the RandomGen class, focussing on
    checking correctness of the next_num function.
    """
    def test_only_returns_values_in_input_values_list(self):
        test_values = [1, 2, 3, 4, 5]
        test_probabilities = [1.0/len(test_values)] * len(test_values)
        generator = nextnum.RandomGen(test_values, test_probabilities)

        for i in xrange(10000):
            return_value = generator.next_num()
            self.assert_(return_value in test_values)


if __name__ == "__main__":
    unittest.main()
