import os
from datetime import datetime
import time

#Setting some evirement variables. File locations.
FTPlocal = "/home/jack/website/html/" # The location the updates are pushed to.
sitelocation = "/var/www/html/" # The location the website is hosted from.
logs = "/home/jack/website/logs/" # Where the logs are to be stored.

#First create logfile if non is found
if 'log.txt' not in os.listdir(logs):
    with open(logs + 'log.txt', 'w') as f:
        print("creating logfile")
        f.write(datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + " Creating new logfile. \n")
        f.close()

#If one is found, check the size if another one needs to be made.
file_size = os.path.getsize(logs + 'log.txt')
if file_size > 100000000: # Should be 100mb.
    logCounter = len([name for name in os.listdir(logs) if os.path.isfile(name)])
    print(logCounter)
    cmd = ("mv " + logs + "log.txt " + logs + "log" + logCounter + ".txt") # Will create a new logfile but no max so will just keep making new ones.
    os.system(cmd)
    with open(logs + 'log.txt', 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + " Creating additional logfile. \n")
        print("Creating additional logfile")
        f.close

#Walks the path of both the ftp location and the site location and finds the most recent change date for any file or dir.
ftpmod = (time.ctime(max(os.path.getmtime(root) for root,_,_ in os.walk(FTPlocal))))
sitemod = (time.ctime(max(os.path.getmtime(root) for root,_,_ in os.walk(sitelocation))))

if sitemod < ftpmod:
    try:
        cmd = ("cp -r /var/www/html /home/jack/website/backup/" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) 
        with open(logs + 'log.txt', 'a+') as f:
            f.write("creating backup in /home/jack/website/backup/"+ datetime.now().strftime("%Y-%m-%d-%H-%M-%S" + "\n")) # Logging could be improved maybe.
            f.close
        os.system(cmd)
    except (Exception, ArithmeticError) as e:
        with open(logs + 'log.txt', 'a+') as f:
            message = (type(e).__name__, e.args)
            f.write(datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + " There was an error, force quitting, backup was not created! " + message + "\n")
            print("error 1")
            f.close
            quit()
    try:
        with open(logs + 'log.txt', 'a+') as f:
            f.write("Updating /home/jack/website/html \n") 
            f.close
        cmd = "cp -r /home/jack/website/html /var/www/"
        os.system(cmd)
    except (Exception, ArithmeticError) as e:
        with open(logs + 'log.txt', 'a+') as f:
            message = (type(e).__name__, e.args)
            f.write(datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + " There was an error, force quitting, update was not compleated! " + message + "\n") 
            print("error 2")
            f.close
            quit()
else:
    print("nothing to do.")
