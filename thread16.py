import threading
import time

MAX_CONCURRENT_DOWNLOADS = 1
semaforo = threading.Semaphore(MAX_CONCURRENT_DOWNLOADS)


def task1():
    while True:

        semaforo.acquire()
        print("Tarea 1 ")
        semaforo.release()
        time.sleep(1)


def task2():
    while True:
        semaforo.acquire()
        print(2)
        semaforo.release()
        time.sleep(0.25)


t = threading.Thread(target=task1)
t.start()
t2 = threading.Thread(target=task2)
t2.start()
