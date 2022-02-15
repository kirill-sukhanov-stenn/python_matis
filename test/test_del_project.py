from model.project import Project
import random

def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.name_or_empty) == sorted(new_projects, key=Project.name_or_empty)




