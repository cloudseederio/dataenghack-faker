import pytest

from dataenghack_faker.meetup_member import hello

@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("A. Musing", "Hello A. Musing!"),
        ("traveler", "Hello traveler!"),
        ("projen developer", "Hello projen developer!"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization."""
    assert hello(name) == expected
