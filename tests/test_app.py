from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    # Arrange (organização)
    client = TestClient(app)

    # Act (ação)
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_root_should_return_correct_content_type():
    # Arrange
    expected_content_type = 'application/json'

    # Act
    response = client.get('/')

    # Assert
    assert expected_content_type in response.headers['content-type']


def test_read_root_should_have_message_key():
    # Arrange
    expected_key = 'message'

    # Act
    response = client.get('/')

    # Assert
    assert expected_key in response.json()
