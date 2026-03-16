import pytest

@pytest.mark.parametrize("username, password, expected_result", [
    ("user1", "pass1", "success"),
    ("user2", "wrong", "failure"),
    ("", "", "failure"),
])
def test_login(username: str, password: str, expected_result: str):
    # In a real test, you'd call your application's login function
    # For now, we'll just simulate it
    print(f"Testing {username}/{password}, expecting {expected_result}")
    assert True # Placeholder for real login logic