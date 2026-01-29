from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_hinsight() -> None:
    resp = client.get("/hinsight")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
