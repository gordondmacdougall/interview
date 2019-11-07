from flask import Flask
from flask_cors import CORS
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'mysql://{username}:{password}@{host}:{port}/{database}?charset=utf8&use_unicode=1'.format(
            host=config.DATABASE_HOSTNAME,
            port=config.DATABASE_PORT,
            username=config.DATABASE_USERNAME,
            password=config.DATABASE_PASSWORD,
            database=config.DATABASE_NAME
        )

db = SQLAlchemy(app)
db.create_all()

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    company_id = db.Column(db.ForeignKey('companies.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    company = db.relationship('Company', backref=db.backref('departments', passive_deletes=True))

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    second_name = db.Column(db.String(80), unique=False, nullable=False)

    company_id = db.Column(db.ForeignKey('companies.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    company = db.relationship('Company', backref=db.backref('employees', passive_deletes=True))

@app.route('/companies')
def get_companies():
    companies = db.session.query(Company).all()
    return jsonify({
        'objects': [{
            'id': company.id,
            'name': company.name,
            'departments': ', '.join([dep.name for dep in company.departments]),
            'employees':', '.join([str(emp.id) + ': ' + emp.first_name + ' ' + emp.second_name for emp in company.employees])
        } for company in companies]
    })

@app.route('/companies', methods=['POST'])
def add_company():
    name = request.json.get('name')
    departments = request.json.get('departments')
    employees = request.json.get('employees')
    if name is None:
        return 400, "Name is required"

    new_company = Company()
    new_company.name = name
    db.session.add(new_company)
    db.session.commit()

    for department in departments.split():
        new_department = Department()
        new_department.name = department
        new_department.company_id = new_company.id
        db.session.add(new_department)
        db.session.commit()

    for employee in employees.split(','):
        first_name, second_name = employee.rsplit(None,1)
        new_employee = Employee()
        new_employee.first_name = first_name
        new_employee.second_name = second_name
        new_employee.company_id = new_company.id
        db.session.add(new_employee)
        db.session.commit()
    return "ASdfwf", 201

@app.route('/employees/<employeeId>', methods=['DELETE'])
def delete_employee(employeeId):
    print employeeId
    Employee.query.filter_by(id=employeeId).delete()
    db.session.commit()
    return "ASdfwf", 201

if __name__ == '__main__':
    app.run(debug=True)
