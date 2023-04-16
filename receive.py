from multiprocessing.connection import Listener
from subprocess import PIPE, Popen
import sys
from essential_generators import DocumentGenerator


gen = DocumentGenerator()

from subprocess import PIPE, Popen

sub = Popen(['python', 'beacon_scanner.py', '/dev/tty.usbmodemC9A6DD9E4BC22'], bufsize=1, stdout=PIPE, text=True)



# for line in sub.stdout:
#     print(line, end='')

# client
def child(conn):
    while (True):
        try:
            msg = conn.recv()
        except:
            break
        # this just echos the value back, replace with your custom logic
        # conn.send(msg)
        
        conn.send(sub.stdout)

        # with Popen(['python', 'beacon_scanner.py', '/dev/tty.usbmodemC9A6DD9E4BC22'], bufsize=1, stdout=PIPE, text=True) as sub:
        #     for line in sub.stdout:
        #         print(line, end='')

# server
def mother(address):
    serv = Listener(address)
    while (True):
        client = serv.accept()
        child(client)

mother(('', 5023))
