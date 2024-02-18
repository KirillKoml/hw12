from utils import arrs

import pytest


@pytest.fixture
def data_fixture():
    return [1, 2, 3, 4]


def test_get(data_fixture):
    assert arrs.get(data_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(data_fixture, 2) == 3


def test_slice(data_fixture):
    assert arrs.my_slice(data_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(data_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(data_fixture, -2, -1) == [3]
    assert arrs.my_slice(data_fixture, -2) == [3, 4]
    assert arrs.my_slice(data_fixture, -3, 3) == [2, 3]
    assert arrs.my_slice(data_fixture, 1, -1) == [2, 3]
    assert arrs.my_slice(data_fixture) == [1, 2, 3, 4]
    assert arrs.my_slice([], 1, -1) == []