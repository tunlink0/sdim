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

    def test_run_route_environment(self):
        r = self.build_routes()
        o0 = r.run_route(uri.Uri("sdim://environment/cpu"))
        print(response_success_list(o0))
        o1 = r.run_route(uri.Uri("sdim://environment/memory"))
        print(response_success_list(o1))
        o2 = r.run_route(uri.Uri("sdim://environment/all"))
        print(response_success_list(o2))