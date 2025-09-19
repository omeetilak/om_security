from app import app

def test_home_endpoint():
    """
    Tests the '/' endpoint to ensure it returns the correct string.
    """
    # Create a test client to simulate requests
    client = app.test_client()
    
    # Make a GET request to the home endpoint
    response = client.get('/')

    # Check that the server responded with 200 OK
    assert response.status_code == 200

    # Check that the response data is the expected string
    # Note: response.data is a byte string, so we use b''
    assert response.data == b"Hello, Jenkins!"
