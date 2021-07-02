from flask import request,render_template,Blueprint
from flask_cors import cross_origin
from flask_api import status
import pandas as pd
from .appExceptions import InvalidEmployeeIdException,EmployeeNotFoundException
from . import constants

bp = Blueprint('empDetails',__name__)

@bp.route("/getEmployeeDetails",methods=['GET'])
@cross_origin()
def getEmployeeDetails():
	try:
		employeeId = request.args['employeeId']
		if not employeeId.isnumeric():
			raise InvalidEmployeeIdException()
		employeeId = int(employeeId)
		employeeDf = pd.read_csv('EmpDetails/static/resource_files/employee_details.csv')
		employeeRow = 	employeeDf[employeeDf['EmployeeID'] == employeeId]
		if employeeRow.shape[0] == 0:
			raise EmployeeNotFoundException()
		return {
			'firstName' : employeeRow['FirstName'].values[0],
			'lastName' : employeeRow['LastName'].values[0],
			'city' : employeeRow['City'].values[0],
			'phoneNo' : str(employeeRow['PhoneNo'].values[0])
		}
	except InvalidEmployeeIdException as e:
		return constants.INVALID_EMPLOYEEID_MESSAGE,status.HTTP_400_BAD_REQUEST
	except FileNotFoundError as e:
		return constants.SERVER_CONNECTION_ERROR_MESSAGE,status.HTTP_500_INTERNAL_SERVER_ERROR
	except EmployeeNotFoundException as e:
		return constants.EMPLOYEE_NOT_FOUND_MESSAGE,status.HTTP_404_NOT_FOUND


@bp.route("/home")
@cross_origin()
def home():
	return render_template('empDetails/main.html')
