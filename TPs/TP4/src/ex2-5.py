import os, sys

pid = os.fork()
if pid == 0:
    os.execlp("./ls-wc.sh", ".")