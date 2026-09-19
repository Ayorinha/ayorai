from fastapi.testclient import TestClient

from api.main import app


def test_health_endpoint() -> None:
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["offline"] is True
    assert body["engine"] == "ayorai-oneocr"


def test_ocr_rejects_non_image_payload() -> None:
    response = TestClient(app).post(
        "/v1/ocr",
        content=b"not an image",
        headers={"content-type": "text/plain"},
    )
    assert response.status_code == 415
