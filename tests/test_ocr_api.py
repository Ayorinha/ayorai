from fastapi.testclient import TestClient
from api.main import app

def test_health_endpoint():
    r=TestClient(app).get("/health")
    assert r.status_code==200 and r.json()["offline"] is True

def test_home_endpoint():
    r=TestClient(app).get("/")
    assert r.status_code==200 and "AYORAI" in r.text

def test_ocr_rejects_non_image_payload():
    r=TestClient(app).post("/v1/ocr",content=b"not image",headers={"content-type":"text/plain"})
    assert r.status_code==415
