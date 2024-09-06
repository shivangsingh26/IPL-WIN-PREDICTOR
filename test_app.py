import requests

def test_app_running():
    # Send a request to the Streamlit app
    url = "http://localhost:8501"
    response = requests.get(url)
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Optionally, check if the response contains some basic HTML structure
    # assert "<html>" in response.text.lower(), "Response doesn't contain expected HTML content."
