import importlib.metadata

class VersionUtil:
    def __init__(self, package_name="lib-version"):
        self.package_name = package_name

    def get_version(self):
        try:
            return importlib.metadata.version(self.package_name)
        except importlib.metadata.PackageNotFoundError:
            return "unknown"
