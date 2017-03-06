import unittest
from collections import OrderedDict


class TestDictionaryIsOrdered(unittest.TestCase):
    def test_dictionary_is_ordered(self):
        # GIVEN
        green_python_party = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

        blue_python_party = green_python_party.copy()
        # blue_python_party = green_python_party  <- this one makes another result. see 'equal vs is' test.

        green_python_party["new green python"] = 111
        blue_python_party["new blue python"] = 999
        print("green python party has: " + str(green_python_party))
        print("blue python party has: " + str(blue_python_party))

        is_there_diff = False
        for i in range(100):
            green_python_party[str(i)] = i
            blue_python_party[str(i)] = i
            for green_one, blue_one in zip(green_python_party, blue_python_party):
                # print(green_one, blue_one)
                if is_there_diff is False and green_one != blue_one and green_one != "new green python":
                    print("we found this same index but not same value >> ",
                          green_one + ":" + str(green_python_party[green_one]),
                          blue_one + ":" + str(blue_python_party[blue_one]))
                    print("green python party has: " + str(green_python_party))
                    print("blue python party has: " + str(blue_python_party))
                    is_there_diff = True

        self.assertTrue(is_there_diff)

        # WHEN
        green_python_party = OrderedDict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)])
        blue_python_party = green_python_party.copy()
        green_python_party["new green python"] = 111
        blue_python_party["new blue python"] = 999
        print("green python party has: " + str(green_python_party))
        print("blue python party has: " + str(blue_python_party))

        # THEN
        is_there_diff = False
        for i in range(100):
            green_python_party[str(i)] = i
            blue_python_party[str(i)] = i
            for green_one, blue_one in zip(green_python_party, blue_python_party):
                # print(green_one, blue_one)
                if is_there_diff is False and green_one != blue_one and green_one != "new green python":
                    print("we found this same index but not same value >> ",
                          green_one + ":" + str(green_python_party[green_one]),
                          blue_one + ":" + str(blue_python_party[blue_one]))
                    print("green python party has: " + str(green_python_party))
                    print("blue python party has: " + str(blue_python_party))
                    is_there_diff = True

        self.assertFalse(is_there_diff)

        # TRAIN YOUR PYTHON
        print("""\nTRAIN YOUR PYTHON""",
              """

              list([]) is always ordered but dictionary({}) is not

              """
              )
