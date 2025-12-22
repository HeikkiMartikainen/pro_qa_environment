import pytest

@pytest.fixture
def sample_data():
    # This could be setting up a database connection,
    # launching a browser, or just creating data.
    return {"user": "Heikki", "role": "admin"}

def test_username(sample_data):
    assert sample_data["user"] == "Heikki"