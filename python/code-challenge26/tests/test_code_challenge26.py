from code_challenge26 import __version__
from code_challenge26.insertions import insertion_sort


def test_version():
    assert __version__ == '0.1.0'

def test_sorting():
    reversed_arr = [20,18,12,8,5,-2]
    few_uniques = [5,12,7,5,5,7]
    nearly_sorted = [2,3,5,7,13,11]
    assert insertion_sort(reversed_arr) == [-2, 5, 8, 12, 18, 20]
    assert insertion_sort(few_uniques) == [5, 5, 5, 7, 7, 12]
    assert insertion_sort(nearly_sorted) == [2, 3, 5, 7, 11, 13]


    