class BinUtilWrapper:
    def __init__(self, cli_name):
        self.cli_name = cli_name


def subprocess_console_response(return_code: int, stdout, stderr):
    return {
            "return_code": return_code,
            "stdout": "".join([chr(int(b)) for b in stdout]),
            "stderr": "".join([chr(int(b)) for b in stderr])
    }
