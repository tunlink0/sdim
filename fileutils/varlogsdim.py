from fileutils.FileUtilWrapper import FileUtilWrapper


class FileUtilVarLogSdim(FileUtilWrapper):
    def __init__(self):
        super().__init__("varlogsdim")

    def load(self, reference: str):
        log = []
        reading = False
        for line in self.read("/var/log/sdim.log"):
            if reading:
                log.append(line)
                if line == ">>> log:end":
                    break
            else:
                if line.startswith(f">>> log:{reference}"):
                    log.append(line)
                    reading = True

        if not reading:
            return {
                "reference": "none"
            }

        return {
            "reference": reference,
            "log": "\n".join(log),
        }