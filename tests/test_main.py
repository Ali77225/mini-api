from fastapi.testclient import  TestClient
from app.main import app
client = TestClient(app)
def test_sante():
    r = client.get("/sante")
    assert r.status_code == 200
    assert r.json() == {"statut": "ok"}