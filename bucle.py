import subprocess as sp
import datetime as dt
import time

while True:


 try:
    sp.call("python jot2pondera.py", shell=True)
    time.sleep(20)
 	sp.call("python mapcreator.py", shell=True)
 	time.sleep(20)
    sp.call("git add mapa.html",shell=True)
    time.sleep(20)
    sp.call("git commit -m 'autocommit mapa.html "+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"' ",shell=True)
    time.sleep(20)
    sp.call("git push origin master",shell=True)
      

     

        




