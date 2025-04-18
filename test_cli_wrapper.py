from unittest import TestCase

import cliwrapper


class Testcli_wrapper_dpkg(TestCase):
    def test_list(self):
        cli_dpkg = cli_wrapper.clCliWrapperDpkg()
        packages = cli_dpkg.list()
        #print(len(packages))
        #for p in packages:
        #    print(f"{p.state_desired}{p.state_current}{p.state_error}     {p.name}     {p.version}")


        self.assertGreater(len(packages), 0)
