from sqlalchemy import select

from fastapi_zero.models.models import User


def test_create_user(session):  # Recebe a fixture como parâmetro
    # Arrange
    user = User(
        username='pedros', password='senha123', email='pedros@example.com'
    )

    # Act
    session.add(user)
    session.commit()

    # Assert
    result = session.scalar(select(User).where(User.username == 'pedros'))

    assert result is not None
    assert result.id == 1
    assert result.username == 'pedros'
    assert result.email == 'pedros@example.com'
