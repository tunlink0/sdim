from unittest import TestCase

import cliparser


class Testcli_section_parser(TestCase):
    def test_cli_list_parser(self):
        str = """
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                          Version                                 Architecture Description
+++-=============================-=======================================-============-================================>
ii  ubuntu-advantage-tools        30~22.04                                amd64        management tools for Ubuntu Pro
ii  ubuntu-wsl                    1.481.1                                 amd64        Ubuntu on Windows tools - Windows Subsystem for Linux integration
ii  update-manager-core           1:22.04.10                              all          manage release upgrades
        """
        clp = cli_parser.CliListParser(
            r"^(?P<states>\w\w[\w ])\s+"
            r"(?P<name>[\w-]+)\s+"
            r"(?P<version>[\d\/~\:\.\+]+)\s+"
            r"(?P<arch>\w+)\s+"
            r"(?P<desc>[\s\S]+)")


        out = clp(str.split("\n"))
        self.assertTrue(len(out) == 3)



