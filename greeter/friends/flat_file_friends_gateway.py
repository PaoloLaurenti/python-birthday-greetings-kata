from datetime import datetime
from greeter.friends.friend import Friend
from greeter.friends.friends_gateway import FriendsGateway


class FlatFileFriendsGateway(FriendsGateway):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_friends(self):
        with open(self.file_path) as f:
            lines = f.readlines()[1:]
            return list(map(lambda l: self.line_to_friend(l), lines))

    def line_to_friend(self, line):
        line_data = list(map(lambda d: d.strip(), line.split(",")))
        last_name = line_data[0]
        first_name = line_data[1]
        birthday = datetime.strptime(line_data[2], "%Y/%m/%d").date()
        email = line_data[3]
        return Friend(name=f"{first_name} {last_name}", email=email, birthday=birthday)
