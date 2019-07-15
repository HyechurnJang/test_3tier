'''
Created on 2019. 7. 15.

@author: jzide
'''

import os
import random
import pygics

def workloader(count):
    data = 0
    for i in range(0, count): data = data + random.randrange(1,3)
    exit(0)

@pygics.rest('GET', '/')
def test(req, count=10000, *args):
    pid = os.fork()
    if pid == 0: workloader(count)
    return {'pid' : str(pid)}

pygics.server('0.0.0.0', 8080)