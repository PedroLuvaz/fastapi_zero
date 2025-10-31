from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(
        username='pedros', password='senha123', email='pedros@example.com'
    )

    # Act
    session.add(user)
    session.commit()

    # Assert
    result = session.scalar(select(User).where(User.username == 'pedros'))

    assert asdict(result) == {
        'id': 1,
        'username': 'pedros',
        'password': 'senha123',
        'email': 'pedros@example.com',
        'created_at': time,
        'updated_at': time,
    }
