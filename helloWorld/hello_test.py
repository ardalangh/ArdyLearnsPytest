import pytest as pytest


def test_1() -> None:
    assert 1 == 1

@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 1

@pytest.mark.skipif(4 > 1, reason="0 is not bigger than 1")
def test_should_be_skipped_under_condition() -> None:
    assert 1 == 2

@pytest.mark.xfail
def test_dont_care_about() -> None:
    assert 1 == 1

@pytest.mark.slow
def test_dont_care_about() -> None:
    assert 1 == 1