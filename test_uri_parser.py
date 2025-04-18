from unittest import TestCase

import uri


class Testuri(TestCase):
    def test_uri_no_query_string(self):
        uri = uri_parser.Uri("sdim://yoo/zoo")
        self.assertTrue(uri.scheme == "sdim")
        self.assertTrue(uri.authority == "yoo")
        self.assertTrue(uri.path == "/zoo")
        self.assertTrue(uri.query_string == "")
        self.assertTrue(len(uri.query_list) == 0)

    def test_uri_query_string(self):
        uri = uri_parser.Uri("sdim://yoo/zoo?foo=bar&bar=foo")
        self.assertTrue(uri.scheme == "sdim")
        self.assertTrue(uri.authority == "yoo")
        self.assertTrue(uri.path == "/zoo")
        self.assertTrue(uri.query_string == "foo=bar&bar=foo")
        self.assertTrue(len(uri.query_list) == 2)
        self.assertTrue(uri.query_list[0] == "foo=bar")
        self.assertTrue(uri.query_list[1] == "bar=foo")

