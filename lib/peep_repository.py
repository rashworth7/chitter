from lib.peep import Peep
from datetime import datetime

class PeepRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM peeps ORDER BY timestamp DESC')
        peeps = []
        for row in rows:
            peep = Peep(row['id'], row['message'], datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'), row['user_id'], row['tags'].split(', '))
            peeps.append(peep)
        return peeps
    
    def all_tags(self):
        rows = self._connection.execute('SELECT * FROM tags')
        tags = []
        for row in rows:
            tags.append((row['user_id'], row['peep_id']))
        return tags
    
    def find_user_ids_by_tag(self, tags):
        print(tags)
        user_ids = []
        for username in tags:
            print(username)
            row = self._connection.execute('SELECT id FROM users WHERE username = %s', [username])
            print("row ========")
            print(row)
            user_id = row[0]['id']
            user_ids.append(user_id)
        return user_ids
    
    def add(self, peep):
        id = self._connection.execute('INSERT INTO peeps (message, timestamp, user_id, tags) VALUES (%s, %s, %s, %s) RETURNING id', [peep.message, peep.timestamp, peep.user_id, ', '.join(peep.tags)])

        peep.id = id[0]['id']

        print(peep.tags)
        user_ids = self.find_user_ids_by_tag(peep.tags)
        for id in user_ids:
            self._connection.execute('INSERT INTO tags (user_id, peep_id) VALUES (%s, %s)', [id, peep.id])
        # self._connection.execute('INSERT INTO tags (user_id, peep_id')
        return None
    
    def delete(self, peep_id):
        self._connection.execute('DELETE FROM peeps where id = %s', [peep_id])
        return None
    
    def find_by_id(self, peep_id):
        row = self._connection.execute('SELECT * FROM peeps WHERE id = %s', [peep_id])
        peep = Peep(row[0]['id'], row[0]['message'], datetime.strptime(row[0]['timestamp'],'%Y-%m-%d %H:%M:%S'), row[0]['user_id'], row[0]['tags'].split(', '))
        return peep
    
    def find_by_tag_username(self, username):
        rows = self._connection.execute('SELECT peeps.id, peeps.message, peeps.timestamp, peeps.user_id, peeps.tags ' \
        'FROM peeps ' \
        'JOIN tags ON peeps.id = tags.peep_id ' \
        'JOIN users ON tags.user_id = users.id ' \
        'WHERE users.username = %s', [username])
        
        peeps = []
        for row in rows:
            peep = Peep(row['id'], row['message'], datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'), row['user_id'], row['tags'].split(', '))
            peeps.append(peep)
 
        return peeps