from datetime import datetime
from lib.peep import Peep
from lib.peep_repository import PeepRepository
from lib.user_repository import UserRepository
from lib.user import User

"""
test return all users
"""

def test_all(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    user_repo = UserRepository(db_connection)
    users = user_repo.all()
    assert users == [
        User(1, 'Rich', 'rich9', 'richpass', 'rich@email'),
        User(2, 'Mollie', 'mollie00', 'molliepass', 'mollie@email'),
        User(3, 'Harry', 'harry77', 'harrypass', 'harry@email'),
        User(4, 'Chelsea', 'chelsea14', 'chelseapass', 'chelsea@email')
    ]

"""
add a user
all returns an updated list
"""

def test_add(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    user_repo = UserRepository(db_connection)
    user = User(None, 'Sam', 'sam17', 'sampass', 'sam@email')
    user_repo.add(user)
    users = user_repo.all()
    assert users == [
        User(1, 'Rich', 'rich9', 'richpass', 'rich@email'),
        User(2, 'Mollie', 'mollie00', 'molliepass', 'mollie@email'),
        User(3, 'Harry', 'harry77', 'harrypass', 'harry@email'),
        User(4, 'Chelsea', 'chelsea14', 'chelseapass', 'chelsea@email'),
        User(5, 'Sam', 'sam17', 'sampass', 'sam@email')
    ]

"""
call delete user
removes user from database
check with all
Also removes all peeps by that user
Also removes all tags for that user
"""

def test_delete(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    user_repo = UserRepository(db_connection)
    user_repo.delete(1)
    users = user_repo.all()
    assert users == [
        User(2, 'Mollie', 'mollie00', 'molliepass', 'mollie@email'),
        User(3, 'Harry', 'harry77', 'harrypass', 'harry@email'),
        User(4, 'Chelsea', 'chelsea14', 'chelseapass', 'chelsea@email')
    ]
    # peep_repo = PeepRepository(db_connection)
    # peeps = peep_repo.all()
    # assert peeps == [
    #     Peep(2, "Message 2", datetime.strptime("2023-06-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 2, ['chelsea14']),
    #     Peep(3, "Message 3", datetime.strptime("2023-05-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 3, ['mollie00'])
    # ]

"""
find user by id
returns user object
"""

def test_find_by_id(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    user_repo = UserRepository(db_connection)
    user = user_repo.find_by_id(1)
    assert user == User(1, 'Rich', 'rich9', 'richpass', 'rich@email')


