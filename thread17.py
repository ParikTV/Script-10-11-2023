import threading
from time import sleep

registros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# semaphore to limit the number of threads that can access the list simultaneously to 4
semaphore = threading.Semaphore(value=4)


def procesando_registro(item):
    semaphore.acquire()  # acquire the semaphore
    try:
        sleep(3)  # simulate some processing time
        print(f'Procesando registro {registros}')  # process the item
    finally:  # Make sure we always release the semaphore
        semaphore.release()  # release the semaphore


# create a list of threads to process the items
threads = [
    threading.Thread(target=procesando_registro, args=(item,))
    for item in registros
]
[thread.start() for thread in threads]  # start all threads
[thread.join() for thread in threads]  # wait for all threads to finish
