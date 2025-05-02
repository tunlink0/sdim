from datetime import datetime

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

        out = {}
        in_stdout = False
        in_stderr = False
        for line in log:
            if line == ">>> log:end":
                in_stderr = False
                break
            elif line == ">>> std:out":
                out["stdout"] = ""
                in_stdout = True
            elif line == ">>> std:err":
                out["stderr"] = ""
                in_stdout = False
                in_stderr = True
            elif in_stdout:
                out["stdout"] += f"{line}\n"
            elif in_stderr:
                out["stderr"] += f"{line}\n"
            elif line.startswith(">>> log"):
                _, reference = line.split(":", 1)
                out["reference"] = reference
            elif line.startswith(">>> invoke"):
                _, invoke = line.split(":", 1)
                out["invoke"] = invoke
            elif line.startswith(">>> time"):
                _, time = line.split(":", 1)
                dt_object = datetime.fromtimestamp(float(time))
                out["datetime"] = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        return {
            "reference": out["reference"],
            "log": out,
        }
