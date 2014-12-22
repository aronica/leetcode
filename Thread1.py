#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread, Lock
import httplib
import time
import multiprocessing
import os

__author__ = 'fafu'

value = 1

lock = Lock()


class AddThread(Thread):
    def __init__(self):
        super(AddThread, self).__init__()

    def run(self):
        global value
        global lock
        lock.acquire()
        for i in range(1000):
            value += 1
            time.sleep(0.1)
        lock.release();


def decrease():
    global value
    for i in range(1000):
        value -= 1
        time.sleep(0.2)


def multi_work(sign,locker):
    locker.acquire();
    print(sign,os.getpid())
    locker.release()


def multi():
    record = []
    locker = multiprocessing.Lock()
    for i in range(5):
        process = multiprocessing.Process(target = multi_work,args=('process',locker))
        process.start()
        record.append(process)
    for process in record:
        process.join()

def inputQ(queue):
    info = str(os.getpid())+ '(put):' + str(time.time())
    queue.put(info)

def outputQ(queue,locker):
    info = queue.get()
    locker.acquire()
    print (str(os.getpid()) + 'get' + info)
    locker.release()




def main():
    record1 = []
    record2 = []
    multiprocessing.Pool()
    locker = multiprocessing.Lock()
    queue = multiprocessing.Queue(3)
    # input processes
    for i in range(10):
        process = multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)

    # output processes
    for i in range(10):
        process = multiprocessing.Process(target=outputQ,args=(queue,locker))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()  # No more object will come, close the queue

    for p in record2:
        p.join()
    # multi()
    # thread1 = AddThread()
    # thread2 = Thread(target=decrease)
    # thread1.start()
    # thread2.start()
    #
    # while True:
    #     print value
    #     time.sleep(1)
    # conn = httplib.HTTPConnection("www.baidu.com")
    # conn.request("get","/")
    # print conn.getresponse().read()




if __name__ == "__main__":
    main()
