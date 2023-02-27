import requests


def test_index_api():
    response = requests.get("http://localhost:5000/api/club/disciplines/")
    data = response.json()["data"]

    assert response.status_code == 200
    assert len(data) == 7
    assert data[0]["name"] == "Futbol"
    assert data[0]["teacher"] == "Juan"
    assert data[0]["dates"] == "Lunes 6:00pm - 8:00pm"


def test_index_api_costs():
    response = requests.get(
        "http://localhost:5000/api/club/disciplines/disciplines_with_costs"
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 7
    assert data[0]["name"] == "Futbol"
    assert data[0]["teacher"] == "Juan"
    assert data[0]["dates"] == "Lunes 6:00pm - 8:00pm"
    assert data[0]["monthly_cost"] in ["800.0", "800"]
    assert data[0]["category"] == "12 a 14 años"
