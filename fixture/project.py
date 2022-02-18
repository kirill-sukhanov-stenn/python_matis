import time
from model.project import Project
import random
import string


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.project_cache = None

    def select_contact_by_name(self):
        wd = self.app.wd
        element = wd.find_elements_by_css_selector("tr[class*='row']")
        cells = element.find_elements_by_tag_name("td")
        return len(cells[0].text)


    def del_project(self, name):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(2)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(2)
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        list = wd.find_elements_by_css_selector("div.col-md-12>div.widget-box div.table-responsive tbody tr")
        return len(list)


    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("tr[class*='row']"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                self.project_cache.append(Project(name=name))
            self.project_cache.pop(0)
        return list(self.project_cache)

    def random(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])