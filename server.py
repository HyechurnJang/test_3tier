'''
Created on 2019. 7. 15.

@author: jzide
'''

import os
import time
import random
import pygics

def workloader(weight):
    data = 0
    for _ in range(0, weight * 10000):
        data = data + random.randrange(1,3)
    exit(0)
    
@pygics.rest('GET', '/')
def test(req, weight=1, *args):
    count = int(weight)
    pid = os.fork()
    if pid == 0: workloader(weight)
    return {'pid' : str(pid), 'weight' : str(count)}

pygics.server('0.0.0.0', 8080)