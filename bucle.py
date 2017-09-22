import subprocess32
#import subprocess.Popen

while True:

 try:
 	  output1 = subprocess32.checkoutput("git pull", shell = True, timeout = 3000)
 	  output2 = subprocess32.checkoutput("git commit -m", shell = True, timeout = 3000)
 	  output3 = subprocess32.checkoutput("git push", shell = True, timeout = 3000)
	
 except subprocess32 as e:
 	print e 




 #args1 = [("git"), ("pull") , shell = True, timeout = 3000]
 #args2 = [("git"), ("commit"), ("-m"), shell = True, timeout = 3000]
 #args3 = [("git"), ("push"), shell = True, timeout = 3000]

 #task1 = subprocess.Popen(args1)
 #task2 = subprocess.Popen(args2)
 #task3 = subprocess.Popen(args3)



