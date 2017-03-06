import unittest
import threading


def remover(list_or_dic):
    if isinstance(list_or_dic, list):
        list_or_dic.pop()
    else:
        list_or_dic.pop(list(list_or_dic.keys())[0])


class TestListAndDicInLoop(unittest.TestCase):
    def test_list_and_dic_in_loop(self):
        # GIVEN
        LOOP_TIME = 100
        python_list = list(range(LOOP_TIME))
        python_dic = dict(list(zip(python_list, python_list)))

        thread_one = None
        loop_times = 0

        for i in python_list:
            if thread_one is None:
                thread_one = threading.Thread(target=remover, args=(python_list,))
                thread_one.start()

            loop_times += 1
            # print(i)

        if thread_one is not None:
            thread_one.join()

        print("loop times: " + str(loop_times))

        # WHEN
        thread_one = None
        loop_times = 0

        for i in python_dic.copy():
            if thread_one is None:
                thread_one = threading.Thread(target=remover, args=(python_dic,))
                thread_one.start()

            loop_times += 1
            # print(i)

        if thread_one is not None:
            thread_one.join()

        print("loop times: " + str(loop_times))

        # THEN
        self.assertEqual(LOOP_TIME, loop_times)

        # TRAIN YOUR PYTHON
        print("""\nTRAIN YOUR PYTHON""",
              """

              You really want changing size of list or dictionary during iteration?
              or not, just Use ".copy()"
              and never try this to dictionary

              """
              )
