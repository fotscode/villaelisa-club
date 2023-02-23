import requests
import pytest

def test_my_disciplines_without_credentials():
    response = requests.get("http://localhost:5000/api/me/disciplines/")
    data = response.json()
    assert response.status_code == 401
    assert len(data) == 1
    assert data["msg"] != ""

    
def test_my_disciplines_with_credentials_with_data():

    #mylogindata={ "username": "admin", "password": "admin"  }
    #login = requests.post("http://localhost:5000/api/auth/login",data=mylogindata)
    #print(login.status_code)
    response = requests.get("http://localhost:5000/api/me/disciplines/")
    print(response)
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 7

def test_my_disciplines_with_credentials_empty():

    #mylogindata={ "username": "admin", "password": "admin"  }
    #login = requests.post("http://localhost:5000/api/auth/login",data=mylogindata)
    #print(login.status_code)
    response = requests.get("http://localhost:5000/api/me/disciplines/")
    print(response)
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 0
    

def test_my_license_without_credentials():
    response = requests.get("http://localhost:5000/api/me/license")
    print(response)
    assert response.status_code == 401
    data = response.json()
    assert len(data) == 1
    assert data["msg"] != ""

def test_my_license_with_credentials():
    response = requests.get("http://localhost:5000/api/me/license")
    print(response)
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 7
    assert data[0]["name"] == "Futbol"
    assert data[0]["teacher"] == "Juan"
    assert data[0]["dates"] == "Lunes 6:00pm - 8:00pm"
    assert data[0]["monthly_cost"] == "800"
    assert data[0]["category"] == "12 a 14 años"