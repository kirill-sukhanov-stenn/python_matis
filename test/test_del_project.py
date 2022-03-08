from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.get_projects()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.soap.get_projects()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    new_projects = app.soap.get_projects()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.name_or_empty) == sorted(new_projects, key=Project.name_or_empty)
