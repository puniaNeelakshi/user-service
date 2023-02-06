from flask import request, Blueprint, jsonify

student_api = Blueprint('student', __name__)


@student_api.route('/student', methods=["POST"])
def add_student():  # put application's code here
    firstname = request.json['first-name']
    lastname = request.json['last-name']
    subject = request.json['subject']

    name = concatName(firstname, lastname)
    message_string = addStudentData(name, subject)
    response = jsonify({'message': message_string})
    return response, 201


def concatName(firstname, lastname):
    name = firstname + '_' + lastname
    return name


def addStudentData(name, subject):
    response = "{} added successfully with subject {}".format(name, subject)
    return response


@student_api.route('/student/<studentId>/marks/<int:marks1>/<int:marks2>')
def get_marks_average(studentId, marks1, marks2):
    result = calculate_formula_marks(marks1, marks2)
    return jsonify({'student-id': studentId, 'formula-marks': result}), 200


def calculate_formula_marks(marks1, marks2):
    value = apply_formula(marks1, marks2)
    return value / 2


def apply_formula(m1, m2):
    product = m1 * m2
    sum_of = m1 + m2
    return sum_of * product
