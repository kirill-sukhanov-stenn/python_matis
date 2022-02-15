from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_project_list()
    name = app.project.random("name", 13)
    if any([p.name == name for p in old_projects]):
        name = app.project.random("name", 13)
    project = Project(name=name)
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.name_or_empty) == sorted(new_projects, key=Project.name_or_empty)
    print(old_projects)