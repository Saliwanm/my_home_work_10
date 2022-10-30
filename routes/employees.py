from app import app, db
from flask import render_template, request, redirect
from models.models import Employee


@app.route('/add-employee')
def add_employee():
    return render_template("add_employee.html")


# @app.route('/plant-info/<int:id>')
# def plant_info():
#     return render_template("plant_info.html")
#
#
@app.route('/save-employee', methods=['POST'])
def save_employee():
    name = request.form.get('name')
    object_id = request.form.get('object_id')
    type_of_work = request.form.get('type_of_work')
    employee = Employee(name=name, object_id=object_id, type_of_work=type_of_work)#ми створили новий обєкт, тобто ми зробили інсерт(insert) в базу даних
    db.session.add(employee)#тут ми добавляємо елемент (employee) у трансакцію
    db.session.commit()
    return redirect('/')
#
#
# @app.route('/delete-plant/<int:id>')
# def delete_plant(id):
#     plant = Plant.query.get(id)#get бере конкретний обєкт у нашому випадку по id
#     db.session.delete(plant)
#     db.session.commit()
#     return redirect('/')