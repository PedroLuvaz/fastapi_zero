from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # Act (ação)
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_root_should_return_correct_content_type(client):
    # Arrange
    expected_content_type = 'application/json'

    # Act
    response = client.get('/')

    # Assert
    assert expected_content_type in response.headers['content-type']


def test_read_root_should_have_message_key(client):
    # Arrange
    expected_key = 'message'

    # Act
    response = client.get('/')

    # Assert
    assert expected_key in response.json()


"""
def test_exercicio_ola_mundo_em_html():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/pedro')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
    assert 'text/html' in response.headers['content-type']
"""


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'pedro',
            'email': 'pedro@example.com',
            'password': 'string',
        },
    )
    # Assert
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'pedro',
        'email': 'pedro@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'pedro',
                'email': 'pedro@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'pedro_updated',
            'email': 'pedroupdate@example.com',
            'password': 'string',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'pedro_updated',
        'email': 'pedroupdate@example.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/999',
        json={
            'username': 'nonexistent',
            'email': 'nonexistent@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted successfully'}


def test_delete_user_not_found(client):
    response = client.delete('/users/666')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
