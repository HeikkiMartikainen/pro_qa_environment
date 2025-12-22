import pytest
import requests

# The base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Use parametrize to run the test for each endpoint in the list
@pytest.mark.parametrize("endpoint, expected_id", [
    ("/posts/1", 1),
    ("/posts/2", 2),
])

def test_get_specific_post(endpoint: str, expected_id: int):
    """
    Tests that we can fetch a specific post and verify its ID.
    """
    # Construct the full URL for the request
    full_url = f"{BASE_URL}{endpoint}"
    
    # Make the API call to the specific endpoint
    response = requests.get(full_url)
    
    # 1. Assert that the request was successful
    assert response.status_code == 200
    
    # 2. Parse the JSON response into a Python dictionary
    response_data = response.json()
    
    # 3. Assert that the 'id' in the response matches the one we expect
    assert response_data["id"] == expected_id