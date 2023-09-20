import time
import threading

"""
线程示例
"""

lock = threading.Lock()


def thread_entry(begin, end):
    for i in range(begin, end):
        time.sleep(1)
        lock.acquire()
        print(i)
        lock.release()


print('\n----------- 线程的构造和使用 -----------')
t0 = threading.Thread(name='thread-0', target=thread_entry, args=(1, 4))
t1 = threading.Thread(name='thread-1', target=thread_entry, args=(100, 104))
t0.start()
t1.start()
t0.join()  # 主线程阻塞，等待 t0 执行完毕
t1.join()  # 主线程阻塞，等待 t1 执行完毕
