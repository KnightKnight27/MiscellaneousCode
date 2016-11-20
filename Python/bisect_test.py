import bisect
import unittest


class TestBisectLeft(unittest.TestCase):

    def test_finding_element_which_is_in_list(self):
        the_list = [1,2,3,4,5]
        self.assertEqual(bisect.bisect_left(the_list, 2), 1)

    def test_finding_element_which_is_not_in_list(self):
        the_list = [1,2,4,5]
        self.assertEqual(bisect.bisect_left(the_list, 3), 2)

    def test_gives_same_result_as_bisect_right_if_item_is_not_in_list(self):
        the_list = [1,2,4,5]
        self.assertEqual(bisect.bisect_left(the_list, 3), bisect.bisect_right(the_list, 3))

    def test_returns_index_of_item_if_item_is_in_list(self):
        the_list = [1,2,4,5]
        self.assertEqual(bisect.bisect_left(the_list, 2), 1)

    def test_returns_index_of_leftmost_item_if_item_is_in_list_multiple_times(self):
        the_list = [1,2,2,4,5]
        self.assertEqual(bisect.bisect_left(the_list, 2), 1)

    def test_returns_zero_if_searching_empty_list(self):
        the_list = []
        self.assertEqual(bisect.bisect_left(the_list, 2), 0)


class TestBisectRight(unittest.TestCase):

    def test_finding_element_which_is_in_list(self):
        the_list = [1,2,3,4,5]
        self.assertEqual(bisect.bisect_right(the_list, 2), 2)

    def test_finding_element_which_is_not_in_list(self):
        the_list = [1,2,4,5]
        self.assertEqual(bisect.bisect_right(the_list, 3), 2)

    def test_gives_same_result_as_bisect_left_if_item_is_not_in_list(self):
        the_list = [1,2,4,5]
        self.assertEqual(bisect.bisect_right(the_list, 3), bisect.bisect_left(the_list, 3))

    def test_returns_one_greater_than_index_of_item_if_item_is_in_list(self):
        the_list = [1,2,4,5]
        self.assertEqual(bisect.bisect_right(the_list, 2), 2)

    def test_returns_one_greater_than_index_of_righttmost_item_if_item_is_in_list_multiple_times(self):
        the_list = [1,2,2,4,5]
        self.assertEqual(bisect.bisect_right(the_list, 2), 3)


class TestBisect(unittest.TestCase):

    def test_bisect_equals_bisect_right(self):
        self.assertEqual(bisect.bisect, bisect.bisect_right)

    def test_bisect_does_not_equal_bisect_left(self):
        self.assertNotEqual(bisect.bisect, bisect.bisect_left)

    def test_returns_zero_if_searching_empty_list(self):
        the_list = []
        self.assertEqual(bisect.bisect_right(the_list, 2), 0)

if __name__ == "__main__":
    unittest.main()
