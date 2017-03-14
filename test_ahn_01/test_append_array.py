import unittest


class TestAddToListCorruption(unittest.TestCase):
    def test_make_list_corruption(self):
        # 무한 루프 생성의 위험

        # GIVEN
        origin_list1 = list(range(10))
        count1 = 0
        for index, value in enumerate(origin_list1):
            """ for loop 안에서 origin_list1 에 아이템을 추가할 경우 enumerate() 에서도 간섭이 일어남.
             enumerate() 시점에서 다른 객체로 생성될 것으로 인식을 하고 사용한 경우임. """
            if index == len(origin_list1) - 1:
                origin_list1.append(value + 1)
            count1 += 1

        # WHEN
        origin_list2 = list(range(10))
        count2 = 0
        for index, value in enumerate(origin_list2[:]):
            """ 간섭이 일어날 수 있는 list 를 enumerate() 할 경우 copy를 사용하자. """
            if index == len(origin_list2) - 1:
                origin_list2.append(value + 1)
            count2 += 1

        self.assertNotEqual(count1, count2)


