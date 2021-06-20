import os
import time
FTPlocal = "/home/jack/website/html"
sitelocation = "/var/www/html"

statbuf = os.stat(FTPlocal)
ftpmod = int((statbuf.st_mtime))
statbuf = os.stat(sitelocation)
sitemod = int((statbuf.st_mtime))
print("Without /")
print(ftpmod)
print(sitemod)
FTPlocal = "/home/jack/website/html/"
sitelocation = "/var/www/html/"
if sitemod < ftpmod:
    print("would update")
else:
    print("NO UPDATE!")
print("With /")
statbuf = os.stat(FTPlocal)
ftpmod = int(statbuf.st_mtime)
statbuf = os.stat(sitelocation)
sitemod = int(statbuf.st_mtime)
print(ftpmod)
print(sitemod)


if sitemod < ftpmod:
    print("would update")
else:
    print("NO UPDATE!")

maindir = "/home/jack/website/html"
altdir = "/var/www/html"

for root, dirs, files in os.walk(maindir):
    for name in files:
        fpath = os.path.join(root, name)
        statbuf = os.stat(fpath)
        print(fpath + ", " + str(statbuf.st_mtime))
    for name in dirs:
        fpath = os.path.join(root, name)
        statbuf = os.stat(fpath)
        print(fpath + ", " + str(statbuf.st_mtime))

ftpmod = (time.ctime(max(os.path.getmtime(root) for root,_,_ in os.walk(FTPlocal))))
sitemod = (time.ctime(max(os.path.getmtime(root) for root,_,_ in os.walk(sitelocation))))

if sitemod < ftpmod:
    print("update")
else:
    print("No update")
