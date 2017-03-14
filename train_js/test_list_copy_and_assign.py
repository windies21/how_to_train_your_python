import unittest

class TestListCopyAndAssign(unittest.TestCase):
    def test_list_copy_and_assign(self):

        #GIVEN
        sample = [[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8]]
        number_list = [1,2,3,4,5,6,7,8,9]

        y_idx = 0

        while y_idx < len(sample):
            targets_list = sample[y_idx]
            assigned_list = number_list
            print("*** number_list assign to assigned_list")

            for x in targets_list:
                try:
                    assigned_list.pop(assigned_list.index(x))
                except (IndexError, ValueError) as e:
                    print("Error message : " + str(e))
                    print("targets_list(%s) : %s" % (str(id(targets_list)),str(targets_list)))
                    print("number_list(%s) : %s" % (str(id(number_list)),str(number_list)))
                    print("assigned_list(%s) : %s" % (str(id(assigned_list)),str(assigned_list)))
                    break
            y_idx += 1

        print("\n")

        #WHEN
        number_list = [1,2,3,4,5,6,7,8,9]
        y_idx = 0
        while y_idx < len(sample):
            targets_list = sample[y_idx]
            copy_list = number_list.copy()
            print("*** number_list copy to copy_list")
            print("targets_list(%s) : %s" % (str(id(targets_list)),str(targets_list)))
            print("number_list(%s) : %s" % (str(id(number_list)),str(number_list)))
            print("copy_list(%s) : %s" % (str(id(copy_list)),str(copy_list)))

            for x in targets_list:
                try:
                    copy_list.pop(copy_list.index(x))
                except (IndexError, ValueError) as e:
                    pass

            y_idx += 1

        #THEN
        copy_list = number_list.copy()
        self.assertNotEqual(id(number_list), id(copy_list))