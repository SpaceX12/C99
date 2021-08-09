import os
import shutil
import time

days = 20
seconds = time.time() - (days*24*60*60)
path = input('Which files to remove:-')

def getTime():
    ctime = os.stat(path).st_ctime
    return ctime

getTime()

os.path.exists(path)

if seconds > days :
    os.remove(path)
else:
    print('The required path does not exist')
 