import os, sys 
n=10 
try: 
    pid = os.fork()
    n+=1

    if pid == 0: #filho
        n /= 2
    else: #pai
        n *= 2
    print ("hello, n=", n) 
except OSError as e: 
    print >>sys.stderr, "fork failed ", e.errno, "-", e.strerror  
    sys.exit(1)