import yaml

class VersionUtil:
    def __init__(self, package_name="lib-version"):
        self.package_name = package_name

    def get_version_from_yaml(self, file_path="version.yaml"):
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
            return data.get("version", "unknown")
    
