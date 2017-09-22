import subprocess as sp
import os
import datetime as dt
import time
from jot2pondera import jot2pondera
from mapcreator import mapcreator

sd = raw_input("serve (1) or do (0)")

sd = int(sd)
if sd == 1:
    while True:
        print("Get Data Ready...")
        time.sleep(90)
        print("Getting Survey Data")
        jot2pondera()
        print("\tDone!")
        time.sleep(60)
        print("Creating Map...")
        mapcreator()
        print("\tDone!")
        time.sleep(55)
        print("Gitting...")
        print("\tAdd")
        sp.call("git add mapa.html", shell=True)
        print("\t\tDone!")
        time.sleep(5)
        print("\tCommit")
        sp.call("git commit -m 'autocommit mapa.html " +
                dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "' ", shell=True)
        print("\t\tDone!")
        time.sleep(10)
        print("\tPushing")
        sp.call("git push origin master", shell=True)
        print("\t\tDone!")
        print(dt.datetime.now())
        print("Till next time...")
        time.sleep(590)
if sd == 0:

    print("Cleaning and Getting Survey Data")
    sp.call("csvclean db_jot.csv",shell=True)
    time.sleep(5)
    sp.call("rm db_jot.csv & mv db_jot_out.csv db_jot.csv",shell=True)
    jot2pondera()
    print("\tDone!")
    time.sleep(5)
    print("Creating Map...")
    mapcreator()
    print("\tDone!")
    time.sleep(5)
    print("Gitting...")
    print("\tAdd")
    sp.call("git add mapa.html", shell=True)
    print("\t\tDone!")
    time.sleep(5)
    print("\tCommit")
    sp.call("git commit -m 'autocommit mapa.html " +
            dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "' ", shell=True)
    print("\t\tDone!")
    time.sleep(5)
    print("\tPushing")
    sp.call("git push origin master", shell=True)
    print("\t\tDone!")
    print(dt.datetime.now())
