from unittest import TestCase

import controller
import router
import uri
from response import response_success_list


class TestRouter(TestCase):
    def build_routes(self):
        r = router.Router()
        r.add_route(router.Route(
            "packages", "/list", router.Endpoint(controller.CliDpkgController())
        ))
        r.add_route(router.Route(
            "environment", "*", router.Endpoint(controller.HostEnvController())
        ))
        return r

    def test_run_route(self):
        r = self.build_routes()
        out = r.run_route(uri.Uri("sdim://packages/list"))
        print(response_success_list(out))
        out = r.run_route(uri.Uri("sdim://packages/list"))
        print(response_success_list(out))

    def test_run_route_environment(self):
        r = self.build_routes()
        o0 = r.run_route(uri.Uri("sdim://environment/cpu"))
        print(response_success_list(o0))
        print(response_success_list(r.run_route(uri.Uri("sdim://environment/cpu"))))
        o1 = r.run_route(uri.Uri("sdim://environment/memory"))
        print(response_success_list(o1))
        o2 = r.run_route(uri.Uri("sdim://environment/version"))
        print(response_success_list(o2))
        o3 = r.run_route(uri.Uri("sdim://environment/uptime"))
        print(response_success_list(o3))
        oall = r.run_route(uri.Uri("sdim://environment/all"))
        print(response_success_list(oall))

    def test_run_route_none(self):
        r = self.build_routes()
        self.assertIsNone(r.run_route(uri.Uri("sdim://notexists/all")))
        self.assertIsNone(r.run_route(uri.Uri("sdim://environment/notexists")))