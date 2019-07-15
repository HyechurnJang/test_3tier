'''
Created on 2019. 7. 15.

@author: jzide
'''

import pygics

@pygics.rest('GET', '/')
def test(req, *args):
    return {'result' : 'OK'}

pygics.server('0.0.0.0', 8080)