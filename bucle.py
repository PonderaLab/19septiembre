import subprocess as sp
import datetime as dt

while True:


 try:

 	sp.call("python mapcreator.py", shell=True)
 	delay(1200000)
    sp.call("git add mapa.html",shell=True)
    delay(600000)
    sp.call("git commit -m 'autocommit mapa.html "+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"' ",shell=True)
    delay(600000)
    sp.call("git push origin master",shell=True)
      

     

        




