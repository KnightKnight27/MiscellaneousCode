"""
Preparation for Phone Interview

Answer the questions below, and send them back via email ahead of the phone
interview. At the phone interview, please have your homework in front of you
and be prepared to discuss your answers with the interviewer.

Algorithms

Implement the method nextNum() and a minimal but effective set of unit tests.
Implement in the language of your choice, Python is preferred, but Java and
other languages are completely fine. Make sure your code is exemplary, as if
it was going to be shipped as part of a production system.

As a quick check, given Random Numbers are [-1, 0, 1, 2, 3] and Probabilities
are [0.01, 0.3, 0.58, 0.1, 0.01] if we call nextNum() 100 times we may get the
following results. As the results are random, these particular results are
unlikely.

-1: 1 times
0: 22 times
1: 57 times
2: 20 times
3: 0 times

Languages Python
You may use random.random() which returns a pseudo random number between 0
and 1.
"""
from __future__ import division
import bisect
import collections
import random


def cumulative_sum(values):
    """
    Returns a list containing the cumulative sum of the
    input values. For example, given

    [0.1,0.2,0.2,0.5]

    returns

    [0.1,0.3,0.5,1.0]
    """
    cumulative_values = []
    cumulative_value = 0.0

    for value in values:
        cumulative_value += value
        cumulative_values.append(cumulative_value)

    return cumulative_values


def find_index_of_leftmost_value_greater_than_x(values, x):
    """
    Utility function to search a sorted list and return the
    index of the position of the first value greater than
    the test value.
    """
    index = bisect.bisect_right(values, x)

    if index != len(values):
        return index
    else:
        raise StandardError(
            "Cannot find valid index for {} in {}".format(x, values)
            )


class RandomGen(object):

    def __init__(self, random_nums, probabilities):
        """
        Initialise the random number generator with a set of allowed numbers,
        and probabilities for each number to occur.
        """
        if any(x < 0.0 for x in probabilities):
            raise StandardError(
                "Negative probabilities ({}) passed".format(probabilities)
                )

        if abs(sum(probabilities) - 1.0) > 1e-10:
            raise StandardError(
                "Probabilities ({}) do not sum to 1.0".format(probabilities)
                )

        if len(random_nums) != len(probabilities):
            raise StandardError(
                "len(probabilities) ({}) != len(random_nums) ({})".format(
                    len(probabilities), len(random_nums)
                ))

        self._random_nums = random_nums
        self._probabilities = probabilities
        self._cumulative_probabilities = cumulative_sum(probabilities)

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        random_value = random.random()
        index_of_number = find_index_of_leftmost_value_greater_than_x(
                              self._cumulative_probabilities,
                              random_value
                          )

        return self._random_nums[index_of_number]


if __name__ == "__main__":
    # Example use-case
    number_of_calls = 1000
    valid_numbers = [1, 2, 3, 4, 5]
    probabilities = [0.1, 0.4, 0.01, 0.001, 0.489]
    generator = RandomGen(valid_numbers, probabilities)
    counter = collections.defaultdict(int)

    for x in xrange(number_of_calls):
        random_number = generator.next_num()
        counter[random_number] += 1

    print("Generated {} random numbers".format(number_of_calls))
    print("Valid values are {}".format(valid_numbers))
    print("Probabilities are {}".format(probabilities))
    print("Printing expected and actual counts for each allowed value")

    for index, number in enumerate(valid_numbers):
        expected = int(number_of_calls * probabilities[index])
        actual = counter[number]
        print(
            "{}: Expected = {}. Actual = {}".format(number, expected, actual)
        )
