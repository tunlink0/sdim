from unittest import TestCase

import binutils.dpkg

class Testcli_wrapper_dpkg(TestCase):
    def test_dpkg_list(self):
        cli_dpkg = binutils.dpkg.BinUtilDpkg()
        packages = cli_dpkg.list()
        self.assertGreater(len(packages), 0)

    def test_id_id(self):
        cli_id = binutils.id.BinUtilId()
        item = cli_id.id()
        self.assertTrue(item.userid == 0)
        self.assertTrue(item.username == "root")
