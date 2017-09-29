import subprocess as sp
import os
import datetime as dt
import time
from jot2pondera import jot2pondera
from mapcreator import mapcreator



sd = raw_input("serve (1) or do (0):\n")

sd = int(sd)

while True:
    print("Getting Survey Data")
    jot2pondera()
    print("\tDone!")
    with open("survey.csv") as f:
        with open("survey.bk") as fb:
            f.next()
            fb.next()
            last = f.next()
            lastbk = fb.next()
    if last!=lastbk:
#        time.sleep(60)
        print("Creating Map...")
        mapcreator()
        print("\tDone!")
#        time.sleep(60)
        # print("Gitting...")
        # print("\tAdd")
#         sp.call("git add mapa.html", shell=True)
#         print("\t\tDone!")
# #        time.sleep(5)
#         print("\tCommit")
#         sp.call("git commit -m 'autocommit mapa.html " +
#                 dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "' ", shell=True)
#         print("\t\tDone!")
#         time.sleep(10)
#         print("\tPushing")
#         sp.call("git push origin master", shell=True)
        # print("\t\tDone!")
        print(dt.datetime.now())
        print("Till next time...")
    else:
        print("no changes")
        print last,"\n",lastbk
        time.sleep(30)
