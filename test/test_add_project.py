from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.get_projects()
    name = app.project.random("name", 13)
    project = Project(name=name)
    app.project.create(project)
    new_projects = app.soap.get_projects()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.name_or_empty) == sorted(new_projects, key=Project.name_or_empty)
    print(old_projects)
