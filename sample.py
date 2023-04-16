
import sys, os

import time
os.environ["PYTHONUNBUFFERED"] = "1"

while True:
    print(time.time(), file=sys.stdout)
    time.sleep(1)