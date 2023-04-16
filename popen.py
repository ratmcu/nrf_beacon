from subprocess import PIPE, Popen
import subprocess, select, os
import time

os.environ["PYTHONUNBUFFERED"] = "1"

proc = subprocess.Popen(['python', 'beacon_scanner.py', '/dev/tty.usbmodemC9A6DD9E4BC22'], stdout=subprocess.PIPE)
poll = select.poll()
poll.register(proc.stdout)

while True:
    pass
    rlist = poll.poll()
    for fd, event in rlist:
        # sys.stdout.write(str(os.read(fd, 1024)))
        ss = str(os.read(fd, 1024).decode())
        if ss != '':
            print(ss.splitlines())

proc.kill()