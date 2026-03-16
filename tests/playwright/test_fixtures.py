import pytest

@pytest.fixture
def sample_data():
    # This could be setting up a database connection,
    # launching a browser, or just creating data.
    return {"user": "Dean", "role": "admin"}

def test_fixtures(sample_data: dict[str, str]) -> None:
    assert sample_data["user"] == "Dean"
    assert sample_data["role"] == "admin"