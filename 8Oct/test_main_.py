from fastapi.testclient import TestClient
from UnitTest import app

client = TestClient(app)  # Arrange


# ---------------- TEST 1 ----------------
def test_get_all_employees():
    response = client.get("/employees")  # ACT
    assert response.status_code == 200  # Assert
    assert isinstance(response.json(), list)  # Assert


# Arrange ACT Assert -- AAA Pattern
# CICD -- Cont Integration -- Cont Deployment -- checkin -- Build -- Test case -- Deployed to QA Server

# -------------- TEST 2 ------------------
def test_add_employee():
    new_emp = {
        "id": 2,
        "name": "Neha Verma",
        "department": "IT",
        "salary": 60000
    }
    response = client.post(url="/employees", json=new_emp)
    assert response.status_code == 201
    assert response.json()["name"] == "Neha Verma"


# -------------- TEST 3 ------------------
def test_get_employee_by_id():
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Amit Sharma"


# -------------- TEST 4 ------------------
def test_get_employee_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


# -------------- TEST 5 ------------------
def test_update_employee():
    # Arrange
    updated_emp = {
        "id": 2,
        "name": "Neha V.",
        "department": "Finance",
        "salary": 65000
    }

    # Act
    response = client.put("/employees/2", json=updated_emp)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Neha V."
    assert data["department"] == "Finance"
    assert data["salary"] == 65000


# -------------- TEST 6 ------------------
def test_delete_employee():
    # Act
    response = client.delete("/employees/2")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Employee with id 2 has been deleted."

    # Extra check: Make sure employee is gone
    follow_up = client.get("/employees/2")
    assert follow_up.status_code == 404
