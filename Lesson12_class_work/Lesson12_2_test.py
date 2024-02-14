import pytest
import Lesson12_2
import user_data


def test_reg_success():
    assert Lesson12_2.registration()==user_data.nick