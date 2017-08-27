# class Room(object):
#
#     def __init__(self,name,description):
#         self.name=name
#         self.description=description
#         self.paths=[]
#
#     def __ge__(self, direction):
#       这一行写错了
#         return  self.paths.get(direction,None)
#
#     def add_paths(self,paths):
#         self.paths.update(paths)

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    def go(self, direction):
        return self.paths.get(direction, None)
    def add_paths(self, paths):
        self.paths.update(paths)
