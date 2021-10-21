import os

pid = os.fork()
if pid == 0:
    os.execlp("/bin/bash", "/bin/bash", "./ls-wc.sh")