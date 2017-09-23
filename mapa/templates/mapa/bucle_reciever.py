import os
import datetime as dt
import time

while True:
    s=135
    print("Pulling...")
    os.system("git pull")
    print("\tDone!")
    time.sleep(10)
    print(dt.datetime.now())
    print("Till next time...")
    time.sleep(s)
