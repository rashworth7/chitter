from lib.peep import Peep
from datetime import datetime

"""
test constructs correctly
"""

def test_construct_peep_no_tags():
    peep = Peep(1, "hi", datetime(2023, 7, 14, 12, 12, 12), 1)
    assert peep.id == 1
    assert peep.message == "hi"
    assert peep.timestamp == datetime(2023, 7, 14, 12, 12, 12)
    assert peep.user_id == 1
    assert peep.tags == []

"""
test peeps with tags
"""
def test_peep_with_tags():
    peep = Peep(1, "hi", datetime(2023, 7, 14, 12, 12, 12), 1, ['Rich', 'Mollie'])
    assert peep.id == 1
    assert peep.message == "hi"
    assert peep.timestamp == datetime(2023, 7, 14, 12, 12, 12)
    assert peep.user_id == 1
    assert peep.tags == ['Rich', 'Mollie']

"""
test objects with same attributes are equal
"""
def test_equal_objects():
    peep1 = Peep(1, "hi", datetime(2023, 7, 14, 12, 12, 12), 1,['Rich'])
    peep2 = Peep(1, "hi", datetime(2023, 7, 14, 12, 12, 12), 1, ['Rich'])
    assert peep1 == peep2

"""
Test object formats correctly
"""
def test_peep_format():
    peep1 = Peep(1, "hi", datetime(2023, 7, 14, 12, 12, 12), 1, ['Rich', 'Mollie'])
    assert str(peep1) == "Peep(1, hi, 2023-07-14 12:12:12, 1, Tags = Rich, Mollie)"
