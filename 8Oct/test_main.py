from fastapi.testclient import TestClient
from course_api import app  # Make sure this matches your actual file name

import pytest

client = TestClient(app)


# ------------------ Task 1: Positive Course Creation ------------------
def test_add_course_success():
    new_course = {
        "id": 2,
        "title": "Data Science",
        "duration": 40,
        "fee": 5000,
        "is_active": True
    }
    response = client.post("/courses", json=new_course)
    assert response.status_code == 201
    assert response.json()["title"] == "Data Science"


# ------------------ Task 2: Duplicate Course ID Handling ------------------
@pytest.mark.parametrize("duplicate_course", [
    {
        "id": 1,  # Already exists in the in-memory list
        "title": "Advanced Python",
        "duration": 50,
        "fee": 8000,
        "is_active": True
    },
    {
        "id": 2,  # Assuming the previous test already added id=2
        "title": "Machine Learning",
        "duration": 60,
        "fee": 10000,
        "is_active": True
    }
])
def test_duplicate_course_id(duplicate_course):
    response = client.post("/courses", json=duplicate_course)
    assert response.status_code == 400
    assert response.json()["detail"] == "Course ID already exists"


# ------------------ Task 3: Validation Error Testing ------------------
def test_course_validation_errors():
    invalid_course = {
        "id": 3,
        "title": "AI Course",
        "duration": 0,
        "fee": -500,
        "is_active": True
    }
    response = client.post("/courses", json=invalid_course)
    assert response.status_code == 422  # Unprocessable Entity

    errors = response.json()["detail"]

    # Check that both 'duration' and 'fee' errors are present
    error_fields = [err["loc"][-1] for err in errors]

    assert "duration" in error_fields
    assert "fee" in error_fields


# ------------------ Task 4: Test GET Returns Correct Format ------------------
def test_get_all_courses_format():
    response = client.get("/courses")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0  # should have at least one course

    for course in data:
        assert isinstance(course, dict)
        assert "id" in course
        assert "title" in course
        assert "duration" in course
        assert "fee" in course
        assert "is_active" in course