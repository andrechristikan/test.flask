from resources.User import UserFindById, UserFindByUsername, User


class Routers:

    def __init__(self, api):
        self.api = api
        self.api.add_resource(UserFindByUsername, '/r/<string:username>')
        self.api.add_resource(UserFindById, '/user/<int:user_id>')
        self.api.add_resource(User, '/user')

    def get(self):
        return self.api
