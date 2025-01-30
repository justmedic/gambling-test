def test_tron_info_endpoint(client):
    response = client.post("/tron-info", json={"address": "TXYZopYRdj2D9XRtbG411X9RuRxWQk8y3C"})
    assert response.status_code == 200
    assert "balance" in response.json()
    assert "bandwidth" in response.json()
    assert "energy" in response.json()


def test_requests_endpoint(client):
    response = client.get("/requests?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json()["items"], list)
