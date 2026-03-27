from fastapi import FastAPI, HTTPException
from models import AppointmentCreate, Status
import service

app = FastAPI(
    title="Appointment API",
    description="API para gestión de citas médicas (MVP)",
    version="1.0.0"
)

# Crear cita
@app.post("/appointments")
def create_appointment(data: AppointmentCreate):
    return service.create_appointment(data)

# Obtener cita por ID
@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    appointment = service.get_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

# Actualizar estado
@app.put("/appointments/{appointment_id}/status")
def update_status(appointment_id: int, status: Status):
    updated = service.update_status(appointment_id, status)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated

# Listar citas
@app.get("/appointments")
def list_all():
    return service.list_appointments()