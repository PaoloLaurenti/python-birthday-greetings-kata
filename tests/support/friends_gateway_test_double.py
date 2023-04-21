from greeter.friends_gateway import FriendsGateway

class FriendsGatewayTestDouble(FriendsGateway):
    def __init__(self):
        self.stubbed_friends = []

    def stub_friends(self, friends):
        self.stubbed_friends.extend(friends)

    def get_friends(self):
        return self.stubbed_friends[:]
