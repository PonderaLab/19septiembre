import subprocess as sp
import datetime as dt

while True:


 try:

      args1 = sp.call("git add mapa.html",shell=True)
      args2 = sp.call("git commit -m 'autocommit mapa.html' ",shell=True)
      dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      args3 = sp.call("git push origin master",shell=True)
      args4 = sp.call("git pull",shell=True)

     

        delay(1800000000)




