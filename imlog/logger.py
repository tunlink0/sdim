import string
import time
import hashlib
import random


class Logger():
    logdir: str = "/var/log"

    def __init__(self):
        self.fp = open(f"{self.logdir}/sdim.log", "w+")

    def log(self, invoker: str, stdout, stderr):
        h1 = time.time()
        h2 = invoker
        h3 = "".join(random.choice(string.ascii_letters) for _ in range(8))
        reference = hashlib.sha256(f"{h1}{h2}{h3}".encode('utf-8')).hexdigest()

        self.fp.write((f">>> log:{reference}\n"
               f">>> invoke:{invoker}\n"
               f">>> time:{h1}\n"
               f">>> std:out\n"
               f"{stdout}\n"
               f">>> std:err\n"
               f"{stderr}\n"
               f">>> log:end\n\n"))
        return reference


class ImLogger:
    logger = Logger()
