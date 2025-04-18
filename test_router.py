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
        return r

    def test_run_route(self):
        r = self.build_routes()
        out = r.run_route(uri.Uri("sdim://packages/list"))
        print(response_success_list(out))