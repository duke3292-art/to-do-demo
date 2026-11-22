import pytest
from todo import TodoList

def test_add():
    t = TodoList()
    assert t.add("장보기") == 0

def test_add_empty():
    with pytest.raises(ValueError):
        TodoList().add("  ")

def test_delete():
    t = TodoList()
    t.add("장보기"); t.add("운동")
    assert t.delete(0)["title"] == "장보기"
    assert [i["title"] for i in t.items] == ["운동"]

def test_delete_invalid_index():
    with pytest.raises(ValueError):
        TodoList().delete(3)
