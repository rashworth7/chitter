from datetime import datetime
from lib.peep_repository import *
from lib.peep import *


"""
test all method returns
a list of peep objects
"""

def test_all_peeps(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    peeps = peeps_repo.all()
    assert peeps == [
        Peep(1, "Message 1", datetime.strptime("2023-07-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 1, ['mollie00', 'harry77']),
        Peep(2, "Message 2", datetime.strptime("2023-06-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 2, ['rich9', 'chelsea14']),
        Peep(3, "Message 3", datetime.strptime("2023-05-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 3, ['mollie00', 'rich9'])
    ]

"""
all tags returns all tags
"""
def test_return_all_tags(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    peeps = peeps_repo.all_tags()
    assert peeps == [
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 1),
        (4, 2)  
    ]

"""
when I have a tag
return the list of uer id's
"""

def test_find_user_ids_from_tag(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    user_ids = peeps_repo.find_user_ids_by_tag(['mollie00', 'harry77'])
    assert user_ids == [2, 3]

"""
When i add a peep
all method returns updated list
"""
def test_add_peep(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    peep = Peep(None, "Message 4", datetime.strptime("2023-07-16 12:12:12", '%Y-%m-%d %H:%M:%S'), 1, ['harry77', 'chelsea14'])
    peeps_repo.add(peep)
    peeps = peeps_repo.all()
    assert peeps == [
        Peep(4, "Message 4", datetime.strptime("2023-07-16 12:12:12", '%Y-%m-%d %H:%M:%S'), 1, ['harry77', 'chelsea14']),
        Peep(1, "Message 1", datetime.strptime("2023-07-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 1, ['mollie00', 'harry77']),
        Peep(2, "Message 2", datetime.strptime("2023-06-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 2, ['rich9', 'chelsea14']),
        Peep(3, "Message 3", datetime.strptime("2023-05-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 3, ['mollie00', 'rich9'])
    ]
    tags = peeps_repo.all_tags()
    assert tags == [
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 1),
        (4, 2),
        (3, 4),
        (4, 4)  
    ] 

"""
test delete peep when given a peep id
"""
def test_delete_peep(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    peeps_repo.delete(3)
    peeps = peeps_repo.all()
    assert peeps == [
        Peep(1, "Message 1", datetime.strptime("2023-07-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 1, ['mollie00', 'harry77']),
        Peep(2, "Message 2", datetime.strptime("2023-06-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 2, ['rich9', 'chelsea14'])
    ]


"""
find peep by id returns specific peep
"""
def test_find_peep_by_id(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    peep = peeps_repo.find_by_id(1)
    assert peep == Peep(1, "Message 1", datetime.strptime("2023-07-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 1, ['mollie00', 'harry77'])


"""
search by tags
return all peeps with that tag
"""
def test_find_peeps_by_tag(db_connection):
    db_connection.seed('seeds/chitter_.sql')
    peeps_repo = PeepRepository(db_connection)
    peeps = peeps_repo.find_by_tag_username('rich9')
    assert peeps == [
        Peep(2, "Message 2", datetime.strptime("2023-06-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 2, ['rich9', 'chelsea14']),
        Peep(3, "Message 3", datetime.strptime("2023-05-14 12:12:12", '%Y-%m-%d %H:%M:%S'), 3, ['mollie00', 'rich9'])
    ]

