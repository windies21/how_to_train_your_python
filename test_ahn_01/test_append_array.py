import unittest


class TestAddToListCorruption(unittest.TestCase):
    def test_make_list_corruption(self):

        # GIVEN
        origin_list1 = list(range(10))
        for index, value in enumerate(origin_list1):
            if index == len(origin_list1) - 1:
                origin_list1.append(value + 1)
            print(origin_list1)

        # WHEN
        origin_list2 = list(range(10))
        for index, value in enumerate(origin_list2[:]):
            if index == len(origin_list2) - 1:
                origin_list2.append(value + 1)
            print(origin_list2)
