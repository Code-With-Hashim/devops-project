"""
Unit tests for the Flask application
"""
import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Project' in response.data

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_info_endpoint(client):
    """Test the info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'application' in data
    assert 'version' in data
    assert 'endpoints' in data

def test_metrics_endpoint(client):
    """Test the metrics endpoint"""
    response = client.get('/api/metrics')
    assert response.status_code == 200
    assert response.content_type == 'text/plain; charset=utf-8'
    assert b'app_requests_total' in response.data

