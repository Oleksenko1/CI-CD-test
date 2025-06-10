from app.main import add
import pytest # noqa: F401

def test_add():
    assert add(2, 3) == 5
    assert add(4, 8) == 12
    assert add(0, 6) == 6
