from multiprocessing.connection import Client
import time

while True:
    c = Client(('localhost', 5023))

    c.send(f'{int(time.time())}')
    print('Got:', c.recv())

    c.send({'a': 123})
    print('Got:', c.recv())
    time.sleep(1)

