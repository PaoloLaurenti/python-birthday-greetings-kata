import tempfile
from datetime import date
from greeter.friends.friend import Friend
from greeter.friends.flat_file.flat_file_friends_gateway import FlatFileFriendsGateway


class TestFlatFileFriendsGateway:
    def test_get_friends_data(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.writelines(
                [
                    b"last_name, first_name, date_of_birth, email, sms\n",
                    b"Franchi, Franco, 1974/04/22, franco@franchi.com, 3331112223\n",
                    b"Luciani, Luciana, 1980/06/11, luciana@luciani.com, 3335556664\n",
                ]
            )
            tmp.seek(0)

            gateway = FlatFileFriendsGateway(tmp.name)

            friends = gateway.get_friends()

            assert friends == [
                Friend(
                    name="Franco Franchi",
                    email="franco@franchi.com",
                    birthday=date(1974, 4, 22),
                    phone_number="3331112223",
                ),
                Friend(
                    name="Luciana Luciani",
                    email="luciana@luciani.com",
                    birthday=date(1980, 6, 11),
                    phone_number="3335556664",
                ),
            ]

    def test_get_no_friends_data_from_empty_file(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.writelines(
                [
                    b"last_name, first_name, date_of_birth, email, sms\n",
                ]
            )
            tmp.seek(0)
            gateway = FlatFileFriendsGateway(tmp.name)

            friends = gateway.get_friends()

            assert len(friends) == 0
