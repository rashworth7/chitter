from lib.peep_repository import *
from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row['id'], row['name'], row['username'], row['password'], row['email'])
            users.append(user)
        return users

    def add(self, user):
        # insert into users
        # return user id
        id = self._connection.execute('INSERT INTO users (name, username, password, email) VALUES (%s, %s, %s, %s) RETURNING id', [user.name, user.username, user.password, user.email])
        user.id = id[0]['id']

    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])

    def find_by_id(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['name'], row['username'], row['password'], row['email'])
        

    # def find_user_by_tag(self, tag):
    #     pass
    