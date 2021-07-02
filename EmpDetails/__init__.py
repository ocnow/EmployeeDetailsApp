from flask import Flask

#create application instance
def create_app():
    app = Flask(__name__)

    from . import employeeDetails
    app.register_blueprint(employeeDetails.bp)
    return app
