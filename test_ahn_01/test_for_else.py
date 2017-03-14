import unittest


class TestForElse(unittest.TestCase):
    def test_for_else(self):
        # GIVEN
        m = 3
        n = 100

        a = set()
        for num in range(m, n + 1):
            for i in range(2, num):
                if num % i == 0:
                    if num in a:
                        a.remove(num)
                    break
                else:
                    a.add(num)

        print(sorted(list(a)), len(list(a)))

        # WHEN
        b = []
        for num in range(m, n + 1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                b.append(num)

        # THEN
        self.assertEqual(len(a), len(b))