from sys import maxsize

class Project:

    def __init__(self, name=None):
        self.name = name
        #self.status = status
        #self.view_state = view_state
        #self.description = description


    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return (self.name == other.name)

    #def id_or_max(self):
    #    if self.id:
    #        return int(self.id)
    #   else:
    #       return maxsize

    def name_or_empty(self):
        if self.name:
            return self.name
        else:
            return ""