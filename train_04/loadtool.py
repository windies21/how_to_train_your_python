#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import coloredlogs
import logging
import sys
import getopt
import timeit
import requests
from multiprocessing import Pool, current_process


class conf:
    # LOGGING ###
    LOG_LEVEL = logging.DEBUG
    LOG_FILE_PATH = "./load_test.log"
    LOG_FORMAT = "'%(asctime)s %(levelname)s %(message)s'"


logging.basicConfig(handlers=[logging.FileHandler(conf.LOG_FILE_PATH, 'w', 'utf-8')],
                    format=conf.LOG_FORMAT, level=conf.LOG_LEVEL)

coloredlogs.install(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


def client_process(argv):
    url = argv[0]
    duration = argv[1]
    method_name = argv[2]

    count_tx = 0
    process_id = str(current_process())
    print("client process id: " + process_id)
    print("duration: " + str(duration))
    print("method_name: " + method_name)

    if method_name == "GET":
        test_data = ""
        test_way = requests.get
    elif method_name == "POST":
        test_data = {
            "task": "something new"
        }
        test_way = requests.post
    else:
        print(method_name + " is not suitable.")
        return

    start_time = timeit.default_timer()
    while duration > (timeit.default_timer() - start_time):
        response = test_way(url, data=test_data)
        # logging.debug("response: " + response.text)

        count_tx += 1
    duration_real = (timeit.default_timer() - start_time)

    # 테스트 측정을 위한 수행 시간 외의 프로그램 수행 시간을 보정한다.
    ops_times = count_tx
    start_time_ops = timeit.default_timer()
    while ops_times > 0:
        # 무조건 성공하는 조건문, while duration > (timeit.default_timer() - start_time): 의 실행 시간 대응
        if 0 < (timeit.default_timer() - start_time):
            ops_times -= 1  # count_tx += 1 실행 시간 대응

    duration_other_ops = timeit.default_timer() - start_time_ops

    print("duration_other_ops: " + str(duration_other_ops))
    duration_real -= duration_other_ops
    print("duration_real: " + str(duration_real))

    return count_tx, duration_real


def log_result(result):
    print("log_result: " + str(result))
    duration_total = 0

    total_tx = 0
    for count_tx, duration in result:
        total_tx += count_tx
        duration_total += duration

    duration_average = duration_total / float(len(result))
    tps_tx = float(total_tx) / duration_average

    # print("total_tx: " + str(total_tx))
    print(str(total_tx), ' transactions are created.')
    print('Creating TXs duration: ', duration_average)
    print('TPS to create Txs: ', tps_tx, 'number of transaction / sec')


def main(argv):
    logging.info("loadtest tool got argv(list): " + str(argv))

    try:
        opts, args = getopt.getopt(argv, "c:u:m:w:t:hd",
                                   ["client=",
                                    "url=",
                                    "mins=",
                                    "help",
                                    "debug"
                                    ])
    except getopt.GetoptError as e:
        logging.error(e)
        usage()
        sys.exit(1)

    # default option values
    client = 1
    url = "http://127.0.0.1:5000/todos"
    duration = 10  # seconds, but param is mins
    test_way = 0

    # apply option values
    for opt, arg in opts:
        if (opt == "-c") or (opt == "--client"):
            client = int(arg)
        elif (opt == "-u") or (opt == "--url"):
            url = arg
        elif (opt == "-m") or (opt == "--mins"):
            duration = int(arg) * 60  # seconds, but param is mins
        elif opt == "-t":
            test_way = int(arg)
        elif (opt == "-h") or (opt == "--help"):
            usage()
            return

    method_name = ["GET", "POST"][test_way]

    # run peer service with parameters
    logging.info("\nTry load test with: \nclient( " +
                 str(client) + " ) \nurl( " +
                 url + " ) \nduration( " +
                 str(duration) + " seconds )\n")

    pool = Pool(processes=client)
    pool.map_async(client_process, (client*((url, duration, method_name),)), callback=log_result)

    logging.debug("wait for duration")
    pool.close()
    pool.join()


def usage():
    print("\n====================================")
    print("USAGE: LoopChain Load Test Tool")
    print("python3 loadtool.py [option] [value] ...")
    print("------------------------------------")
    print("\noption list")
    print("------------------------------------")
    print("-d : set logging level to debug")
    print("-c or --client : num of dummy client")
    print("-u or --url : test url (default is http://127.0.0.1:5000/todos)")
    print("-m or --mins : test duration (mins)")
    print("-t : test method (0: GET, 1: POST)")
    print("-h or --help : show usage\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        main(sys.argv[1:])
