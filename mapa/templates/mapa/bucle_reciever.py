import subprocess as sp
import datetime as dt
import time

while True:
    s=900
    print("Pulling...")
    sp.call("python jot2pondera.py", shell=True)
    print("\tDone!")
    time.sleep(10)
    print(dt.datetime.now())
    print("Till next time...")
    time.sleep(s-10)
