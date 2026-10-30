import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

@pytest.fixture
def auth_client(db):
    return APIClient()

def test_register_and_login_flow(auth_client):
    # Register new user with custom tenant
    reg_res = auth_client.post('/api/auth/register/', {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'SecurePassword123!',
        'tenant_id': 'enterprise_corp'
    }, format='json')
    assert reg_res.status_code == status.HTTP_201_CREATED
    data = reg_res.json()
    assert data['username'] == 'newuser'
    assert data['tenant_id'] == 'enterprise_corp'

    # Login
    login_res = auth_client.post('/api/auth/login/', {
        'username': 'newuser',
        'password': 'SecurePassword123!'
    }, format='json')
    assert login_res.status_code == status.HTTP_200_OK

    # Get profile
    profile_res = auth_client.get('/api/auth/me/')
    assert profile_res.status_code == status.HTTP_200_OK
    assert profile_res.json()['username'] == 'newuser'
    assert profile_res.json()['tenant_id'] == 'enterprise_corp'

    # Logout
    logout_res = auth_client.post('/api/auth/logout/')
    assert logout_res.status_code == status.HTTP_200_OK

def test_login_invalid_credentials(auth_client):
    res = auth_client.post('/api/auth/login/', {
        'username': 'nonexistent',
        'password': 'wrongpassword'
    }, format='json')
    assert res.status_code == status.HTTP_401_UNAUTHORIZED
