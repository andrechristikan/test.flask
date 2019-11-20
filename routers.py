from resources.User import UserFindById, UserFindByUsername, User
from resources.Login import Login


class Routers:

    def __init__(self, api):
        self.api = api
        self.api.add_resource(UserFindByUsername, '/r/<string:username>')
        self.api.add_resource(UserFindById, '/user/<int:id>')
        self.api.add_resource(User, '/user')
        self.api.add_resource(Login, '/login')

    def get(self):
        return self.api
