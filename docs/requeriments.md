# 📋 Requirements

## 📌 Descripción

Este documento define los requisitos del sistema **Sistema de Gestión de Citas Médicas (MVP)**, incluyendo la priorización del backlog utilizando el modelo:

👉 Must / Should / Could / Won’t

---

## 🎯 Requisitos funcionales

### 🔴 Must (Obligatorios)

- El sistema debe permitir crear una cita médica
- El sistema debe permitir consultar una cita por ID
- El sistema debe permitir actualizar el estado de una cita
- El sistema debe validar los datos de entrada
- El sistema debe manejar errores HTTP básicos (400, 404)

---

### 🟡 Should (Importantes)

- El sistema debería permitir listar todas las citas
- El sistema debería devolver respuestas en formato JSON
- El sistema debería documentar la API mediante OpenAPI

---

### 🟢 Could (Deseables)

- El sistema podría tener una estructura modular (models, service, main)
- El sistema podría incluir un README detallado
- El sistema podría prepararse para una base de datos futura

---

### ⚫ Won’t (Fuera de alcance)

- Autenticación y autorización de usuarios
- Base de datos persistente
- Pagos en línea
- Interfaz gráfica (frontend)
- Notificaciones (correo o SMS)

---

## 🧪 Historias de usuario

### 🟥 Historia 1: Crear cita

**Como** usuario  
**Quiero** registrar una cita médica  
**Para** gestionar la atención de pacientes  

**Criterios de aceptación:**
