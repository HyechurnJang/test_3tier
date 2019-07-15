'''
Created on 2019. 7. 15.

@author: jzide
'''

import os
import time
import random
import pygics

def workloader(sec):
    stt = time.time()
    while True:
        data = 0
        for i in range(0, 10000):
            data = data + random.randrange(1,3)
        end = time.time()
        if end - stt > sec: break
    exit(0)

@pygics.rest('GET', '/')
def test(req, sec=1, *args):
    sec = int(sec)
    pid = os.fork()
    if pid == 0: workloader(sec)
    return {'pid' : str(pid)}

pygics.server('0.0.0.0', 8080)