from multiprocessing.connection import Listener
from subprocess import PIPE, Popen
import sys
from essential_generators import DocumentGenerator


from subprocess import PIPE, Popen
import subprocess, select, os
import time

os.environ["PYTHONUNBUFFERED"] = "1"

proc = subprocess.Popen(['python', 'beacon_scanner.py', '/dev/tty.usbmodemC9A6DD9E4BC22'], stdout=subprocess.PIPE)
poll = select.poll()
poll.register(proc.stdout)


# client
def child(conn):
    while (True):
        try:
            msg = conn.recv()
        except:
            break
        # msg = conn.recv()
        # if msg == 
        # this just echos the value back, replace with your custom logic
        # conn.send(msg)
        rlist = poll.poll()
        for fd, event in rlist:
            # sys.stdout.write(str(os.read(fd, 1024)))
            ss = str(os.read(fd, 1024).decode())
            if ss != '':
                print(ss.splitlines())
        try:
            conn.send(ss)
        except: break

        # with Popen(['python', 'beacon_scanner.py', '/dev/tty.usbmodemC9A6DD9E4BC22'], bufsize=1, stdout=PIPE, text=True) as sub:
        #     for line in sub.stdout:
        #         print(line, end='')

# server
def mother(address):
    serv = Listener(address)
    serv._listener._socket.settimeout(1)
    while (True):
        rlist = poll.poll()
        for fd, event in rlist:
            # sys.stdout.write(str(os.read(fd, 1024)))
            ss = str(os.read(fd, 1024).decode())
            if ss != '':
                print(ss.splitlines())
        try:
            client = serv.accept()
            child(client)
        except: pass

mother(('', 5023))
proc.kill()