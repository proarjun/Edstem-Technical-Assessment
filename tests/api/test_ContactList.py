import pytest
from rest_framework.test import APIClient
#from rest_framework import status

client = APIClient()

#test for creating and viewing the contact
@pytest.mark.django_db

def test_create_contact():
    payload = dict(
        full_name = 'Abhinav R',
        address = 'Ernakulam, Kerala',
        phone = 1597538462,
        email = 'abhinav@hotmail.com'
    )

    response = client.post('/contact-list/', payload)

    data = response.data
    assert data["full_name"] == payload["full_name"]
    assert data["address"] == payload["address"]
    assert data["phone"] == payload["phone"]
    assert data["email"] == payload["email"]

#test for deleting the contact
@pytest.mark.django_db

def test_get_contact():
    payload = dict(
        full_name = 'Abhinav R',
        address = 'Ernakulam, Kerala',
        phone = 1597538462,
        email = 'abhinav@hotmail.com'
    )

    variable = client.post('/contact-list/', payload)
    data = variable.data
    
    response = client.delete(f'/contact-list/{data["id"]}')

    assert response.status_code == 204