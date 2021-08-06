import os
import shutil
import time

days = time.time()
path = input('Which files to remove:-')

def getTime():
    ctime = os.stat(path).st_ctime
    return ctime


getTime()

os.path.exists(path)
list_of_files = os.walk(path)
os.path.join(path)

if getTime() > days :
    os.remove(path)
else:
    print('The required path does not exist')
 