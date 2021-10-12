import os, sys

try:
    for i in range(8):
        pid = os.fork()
        
        if pid == 0: #filho
            file=open("TMP"+str(i+1),'w')
            file.close()
            exit()
except OSError as e:
    print >>sys.stderr, "fork failed ", e.errno, "-", e.strerror
    sys.exit(1)