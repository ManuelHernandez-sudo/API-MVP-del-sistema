appointments = {}
counter = 1

def create_appointment(data):
    global counter
    appointment = {
        "id": counter,
        "patient_name": data.patient_name,
        "date": data.date,
        "status": "pending"
    }
    appointments[counter] = appointment
    counter += 1
    return appointment

def get_appointment(appointment_id):
    return appointments.get(appointment_id)

def update_status(appointment_id, status):
    if appointment_id in appointments:
        appointments[appointment_id]["status"] = status
        return appointments[appointment_id]
    return None

def list_appointments():
    return list(appointments.values())