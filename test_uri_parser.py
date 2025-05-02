from unittest import TestCase

import uri


class Testuri(TestCase):
    def test_uri_no_query_string(self):
        u = uri.Uri("sdim://yoo/zoo")
        self.assertTrue(u.scheme == "sdim")
        self.assertTrue(u.authority == "yoo")
        self.assertTrue(u.path == "/zoo")
        self.assertTrue(u.query_string == "")
        self.assertTrue(len(u.query_list) == 0)

    def test_uri_query_string(self):
        u = uri.Uri("sdim://yoo/zoo?foo=bar&bar=foo")
        self.assertTrue(u.scheme == "sdim")
        self.assertTrue(u.authority == "yoo")
        self.assertTrue(u.path == "/zoo")
        self.assertTrue(u.module == "zoo")
        self.assertTrue(u.query_string == "foo=bar&bar=foo")
        self.assertTrue(len(u.query_list) == 2)
        self.assertTrue(u.query_list[0] == "foo=bar")
        self.assertTrue(u.query_list[1] == "bar=foo")

    def test_uri_query_string_mod_modpath(self):
        u = uri.Uri("sdim://yoo/zoo/xoo?foo=bar&bar=foo")
        self.assertTrue(u.scheme == "sdim")
        self.assertTrue(u.authority == "yoo")
        self.assertTrue(u.path == "/zoo/xoo")
        self.assertTrue(u.module == "zoo")
        self.assertTrue(u.modpath == "/xoo")
        self.assertTrue(u.query_string == "foo=bar&bar=foo")
        self.assertTrue(len(u.query_list) == 2)
        self.assertTrue(u.query_list[0] == "foo=bar")
        self.assertTrue(u.query_list[1] == "bar=foo")

