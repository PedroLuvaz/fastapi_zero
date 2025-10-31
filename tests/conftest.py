from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_db_time():
    return _mock_db_time

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
    engine.dispose()


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    def _set_time(mapper, connection, target):
        for attr in ('created_at', 'updated_at'):
            if hasattr(target, attr):
                setattr(target, attr, time)

    event.listen(model, 'before_insert', _set_time)
    event.listen(model, 'before_update', _set_time)

    try:
        yield time
    finally:
        event.remove(model, 'before_insert', _set_time)
        event.remove(model, 'before_update', _set_time)
