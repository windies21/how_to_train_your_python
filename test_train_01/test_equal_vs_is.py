import unittest


class TestEqualVsIs(unittest.TestCase):
    def test_equal_vs_is(self):
        # GIVEN
        little_python_green = [1, 2, 3]
        little_python_blue = little_python_green
        print("Your are same? : " + str(little_python_green == little_python_blue))
        print("Your are same? : " + str(little_python_green is little_python_blue))
        print("result is same because green one is: " + str(id(little_python_green)))
        print("and blue one is: " + str(id(little_python_blue)))

        # WHEN
        little_python_blue = little_python_green[:]
        print("Your are same? : " + str(little_python_green == little_python_blue))
        print("Your are same? : " + str(little_python_green is little_python_blue))
        print("result is not same because green one is: " + str(id(little_python_green)))
        print("and blue one is: " + str(id(little_python_blue)))

        # THEN
        self.assertNotEqual((little_python_green == little_python_blue), (little_python_green is little_python_blue))

        # TRAIN YOUR PYTHON
        print("""\nTRAIN YOUR PYTHON""",
              """

              is checks that 2 arguments refer to the same object,
              == checks that 2 arguments have the same value

              """
              )
