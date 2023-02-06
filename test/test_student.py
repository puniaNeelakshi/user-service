from unittest.mock import patch

from flask import json

import student
from main import app


def test_should_call_student_add_API():
    response = app.test_client().post(
        '/student',
        data=json.dumps({
            "first-name": "Bob",
            "last-name": "Brown",
            "subject": "Hindi"
        }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 201
    assert data['message'] == 'Bob_Brown added successfully with subject Hindi'


def test_should_return_concatenated_name():
    response = student.concatName("Bob", "Brown")
    assert response == "Bob_Brown"


def test_should_return_json_message():
    result = student.addStudentData("Kumar", "Maths")
    assert result == "Kumar added successfully with subject Maths"
    assert not result == "Maths added successfully with subject Kumar"


def test_should_call_get_students_average_marks_api():
    response = app.test_client().get(
        '/student/22/marks/1/3'
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['average-marks'] == 2.0
    assert data['student-id'] == '22'


@patch('student.apply_formula')
def test_should_get_student_average_marks(mock_get):
    mock_get.return_value = 12
    assert student.calculate_formula_marks(1, 3) == 6.0


def test_should_apply_formula_to_calculate_marks():
    result = student.apply_formula(1, 3)
    assert result == 12


