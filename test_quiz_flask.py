import pytest
from app import app  # Assuming your Flask app is in app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test if the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Quiz Game" in response.data

def test_next_question_correct(client):
    """Test the flow with a correct answer."""
    client.get('/')  # Start the quiz
    response = client.post('/next', data={'answer': 'B'})
    assert b"Score: 1" in response.data  # Check if the score is updated correctly

def test_next_question_incorrect(client):
    """Test the flow with an incorrect answer."""
    client.get('/')  # Start the quiz
    response = client.post('/next', data={'answer': 'A'})
    assert b"Score: 0" in response.data  # Check if the score remains the same

def test_quiz_end(client):
    """Test reaching the end of the quiz."""
    client.get('/')  # Start the quiz
    client.post('/next', data={'answer': 'B'})  # First question
    response = client.post('/next', data={'answer': 'C'})  # Last question

    # Adjust the expected message to match what is displayed on the final page
