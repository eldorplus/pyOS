import time
import random

def run(shell, args):
    for x in xrange(20):
        shell.stdout.write(x)
        time.sleep(1*random.random())

def help():
    return ''