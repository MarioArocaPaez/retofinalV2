from app import create_app
from app.models import Data

def test_home_route():
    app = create_app("development")
    client = app.test_client()
    response = client.get('/data')
    assert response.status_code == 200

def test_root_route():
    app = create_app("development")
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    
def test_post_data():
    app = create_app("development")
    client = app.test_client()
    response = client.post('/data', json={"name": "TestName"})
    assert response.status_code == 201
    assert b"TestName" in response.data

def test_post_data_missing_name():
    app = create_app("development")
    client = app.test_client()
    response = client.post('/data', json={})
    assert response.status_code == 400
    assert b"Missing 'name'" in response.data

def test_data_repr():
    d = Data(name="ReprTest")
    assert repr(d) == "<Data ReprTest>"
