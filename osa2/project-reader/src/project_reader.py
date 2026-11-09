from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def _dependency_name(self, dependency):
        return dependency.split(">=")[0]

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        project = data["project"]
        dev_dependencies = data.get("dependency-groups", {}).get("dev", [])

        return Project(
            project["name"],
            project["description"],
            project.get("license"),
            [author["name"] for author in project.get("authors", [])],
            [self._dependency_name(dep) for dep in project.get("dependencies", [])],
            [self._dependency_name(dep) for dep in dev_dependencies],
        )