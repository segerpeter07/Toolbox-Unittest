"""
A simple script that sorts a list of numbers and removes negative
"""
import unittest


def sort_numbers(numbers):
    return sorted(numbers)


def remove_negatives(numbers):
    returns = []
    for num in numbers:
        if num > 0:
            returns.append(num)
    return returns


# Begin test suite
class TestNegativeSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort_numbers([1, 5, 3]), [1, 3, 5])

    def test_negative(self):
        self.assertEqual(remove_negatives([1, -3, 4]), [1, 4])


if __name__ == '__main__':
    numbers = [1, 5, 7, 4, 7, 4, 2, -2, 3, -3, -2, -7, -4, -12, -13]
    sorted_nums = sort_numbers(numbers)
    print(remove_negatives(sorted_nums))
    unittest.main()
