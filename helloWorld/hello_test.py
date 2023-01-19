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


# @pytest.mark.slow
# def test_dont_care_about() -> None:
#     assert 1 == 1


class Company:
    def __init__(self, name: str, stock_sample: str):
        self.name = name
        self.stock_sample = stock_sample

    def __str__(self):
        return f"{self.name}: {self.stock_sample}"


@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_sample="FVRR")


def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")


@pytest.mark.parametrize(
    "company_name",
    ["Instagram", "TickTok", "Twitch"],
    ids=["InstagramTest", "TickTokTest", "TwitchTest"]
)
def test_parametrize(company_name: str) -> None:
    print(f"Test with {company_name}")


def raise_covid19_exception() -> None:
    raise ValueError('Covid Exception')


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "Covid Exception" == str(e.value)
