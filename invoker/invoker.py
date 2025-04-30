import re
import subprocess
from typing import Any

from imlog.logger import ImLogger

class CallbackPattern(object):
    def __init__(self, regex: re.Pattern[Any], cb):
        self.pattern: re.Pattern[Any] = re.compile(regex)
        self.callback = cb

    def check(self, line):
        tup = self.pattern.findall(line)
        if tup:
            self.callback(tup)
            return True
        return False

class CompletedInvoker:
    def __init__(self, stdout: str, stderr: str, reference: str):
        self.stdout = stdout
        self.stderr = stderr
        self.reference = reference
class Invoker(object):
    def __init__(self):
        self.logger = ImLogger.logger
        self.callbacks: list[CallbackPattern] = []

    def run(self, args: list[str], log=False):
        reference = None
        sp = subprocess.run(args, capture_output=True, text=True)

        stdout = sp.stdout
        stderr = sp.stderr
        self.process_callbacks(stdout, stderr)
        if log:
            reference = self.logger.log(" ".join(args), stdout, stderr)
        return CompletedInvoker(stdout, stderr, reference)

    def process_callbacks(self, stdout: str, stderr: str):
        for line in stdout.split("\n"):
            for cbpattern in self.callbacks:
                if cbpattern.check(line):
                    break

    def callback(self, cb, regex: str):
        self.callbacks.append(CallbackPattern(regex, cb))

