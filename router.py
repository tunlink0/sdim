from controllers import controller
import uri


class Endpoint:
    def __init__(self, c: controller.Controller):
        self.controller = c

    def run(self, path: str, query: str):
        return self.controller.run(path, query)


class Route:
    def __init__(self, authority, path, endpoint):
        self.authority = authority
        self.path = path
        self.endpoint = endpoint


class Router:
    def __init__(self):
        self.routes: list[Route] = []

    def add_route(self, r: Route):
        self.routes.append(r)

    def run_route(self, uri: uri.Uri):
        for r in self.routes:
            if r.authority == uri.authority and (r.path == "*" or r.path == uri.path):
                return r.endpoint.run(uri.path, uri.query_string)
        return None
