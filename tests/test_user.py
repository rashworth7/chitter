from lib.user import User

"""
test constructs correctly
"""

def test_user_constructs():
    user = User(1, "name", "username", "password", "email add")
    assert user.id == 1
    assert user.name == "name"
    assert user.username == "username"
    assert user.password == "password"
    assert user.email == "email add"

"""
test formats correctly
"""

def test_user_format():
    user = User(1, "name", "username", "password", "email add")
    assert str(user) == "User(1, name, username, password, email add)"

"""
test equal objects return true
"""

def test_equal_users():
    user1 = User(1, "name", "username", "password", "email add")
    user2 = User(1, "name", "username", "password", "email add")
    assert user1 == user2