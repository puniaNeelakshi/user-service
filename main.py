from flask import Flask

from controller import TeacherAPI
from student import student_api

app = Flask(__name__)
app.register_blueprint(student_api)
app.register_blueprint(TeacherAPI.teacher_api)

if __name__ == '__main__':
    app.run()
