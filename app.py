from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    date = db.Column(db.String(50))
    patient = db.relationship('Patient')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        patient = Patient(name=name, age=age, gender=gender)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patients'))
    all_patients = Patient.query.all()
    return render_template('patients.html', patients=all_patients)

@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        date = request.form['date']
        appointment = Appointment(patient_id=patient_id, date=date)
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('appointments'))
    all_appointments = Appointment.query.all()
    all_patients = Patient.query.all()
    return render_template('appointments.html', appointments=all_appointments, patients=all_patients)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
