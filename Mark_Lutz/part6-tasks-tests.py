import sys

import pytest

sys.path.append('.')
from mylist import MyList

lists = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    ['a', 'b', 'c', 'd'],
    [1, 2, 'a', 'b']]

lists_ids = [str(element) for element in lists]

alist = lists[0]
from_list = MyList(list(alist))
from_alist = MyList(alist)
from_mylist = MyList(MyList(alist))


def test_repr():
    assert str(from_alist) == str(from_alist.data)
    assert str(from_mylist) == str(from_mylist.data)
    assert str(from_list) == str(from_list.data)


def test_init():
    assert type(from_mylist.data) == type(from_list.data)
    assert from_mylist.data == from_list.data
    assert from_mylist.data == from_alist.data


@pytest.mark.parametrize('alist', lists, ids=lists_ids)
def test_contains(alist: list):
    from_list = MyList(list(alist))
    from_alist = MyList(alist)
    from_mylist = MyList(MyList(alist))
    for element in alist:
        assert element in from_alist
        assert element in from_list
        assert element in from_mylist
    for idx, element in enumerate(alist):
        assert element == from_alist[idx]
        assert element == from_list[idx]
        assert element == from_mylist[idx]

