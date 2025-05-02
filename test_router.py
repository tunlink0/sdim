from unittest import TestCase
import router
import uri
from controllers.logcontroller import LogsController
from controllers.packagescontroller import PackagesController
from controllers.environmentcontroller import EnvironmentController
from response import response_success_list


class TestRouter(TestCase):
    def build_routes(self):
        r = router.Router()
        r.add_route(router.Route(
            "packages", "*", router.Endpoint(PackagesController())
        ))
        r.add_route(router.Route(
            "environment", "*", router.Endpoint(EnvironmentController())
        ))

        r.add_route(router.Route(
            "logs", "*", router.Endpoint(LogsController())
        ))
        return r

    def test_run_route(self):
        r = self.build_routes()
        out = r.run_route(uri.Uri("sdim://packages/list"))
        print(response_success_list(out))
        out = r.run_route(uri.Uri("sdim://packages/list"))
        print(response_success_list(out))

    def test_run_packages_update(self):
        r = self.build_routes()
        out = r.run_route(uri.Uri("sdim://packages/update"))
        self.assertTrue(out["return_code"] == 0)
        print(response_success_list(out))

    def test_run_packages_upgradable(self):
        r = self.build_routes()
        out = r.run_route(uri.Uri("sdim://packages/upgradable"))
        print(response_success_list(out))

    def test_run_packages_upgrade(self):
        r = self.build_routes()
        out = r.run_route(uri.Uri("sdim://packages/upgrade"))
        print(response_success_list(out))

    def test_run_route_environment_cpu(self):
        r = self.build_routes()
        o = r.run_route(uri.Uri("sdim://environment/cpu"))
        print(response_success_list(o))

    def test_run_route_environment_memory(self):
        r = self.build_routes()
        o = r.run_route(uri.Uri("sdim://environment/memory"))
        print(response_success_list(o))

    def test_run_route_environment_version(self):
        r = self.build_routes()
        o = r.run_route(uri.Uri("sdim://environment/version"))
        print(response_success_list(o))

    def test_run_route_environment_uptime(self):
        r = self.build_routes()
        o = r.run_route(uri.Uri("sdim://environment/uptime"))
        print(response_success_list(o))

    def test_run_route_environment_all(self):
        r = self.build_routes()
        oall = r.run_route(uri.Uri("sdim://environment/all"))
        print(response_success_list(oall))

    def test_run_route_logs_view_reference(self):
        r = self.build_routes()
        o = r.run_route(uri.Uri("sdim://logs/view/e49700217c3661c69"))
        print(response_success_list(o))

    def test_run_route_none(self):
        r = self.build_routes()
        self.assertIsNone(r.run_route(uri.Uri("sdim://notexists/all")))
        self.assertIsNone(r.run_route(uri.Uri("sdim://environment/notexists")))
