import pytest
from todo import TodoList

def test_add():
    t = TodoList()
    assert t.add("장보기") == 0

def test_add_empty():
    with pytest.raises(ValueError):
        TodoList().add("  ")
