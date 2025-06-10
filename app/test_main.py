from app.main import add
import pytest

def test_add():
    assert add(2, 3) == 5