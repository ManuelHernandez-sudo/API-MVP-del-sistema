# 🏥 Appointment API MVP

Sistema de gestión de citas médicas desarrollado como un **MVP (Minimum Viable Product)** utilizando FastAPI.

---

## 📌 Descripción

Este proyecto implementa una API REST que permite gestionar citas médicas de forma simple, incluyendo:

- Creación de citas
- Consulta de citas por ID
- Actualización de estado
- Listado de citas

El sistema está diseñado como una primera versión funcional enfocada en validar el flujo principal del negocio.

---

## ❗ Problema que resuelve

La gestión manual de citas médicas suele ser:

- Ineficiente
- Propensa a errores
- Difícil de escalar

Esta API permite digitalizar ese proceso mediante un servicio backend simple y accesible.

---

## 🎯 Alcance (Scope)

### ✅ Incluido

- Crear citas médicas
- Consultar citas por ID
- Listar citas
- Actualizar estado de citas
- Validación de datos de entrada
- Manejo básico de errores

### ❌ No incluido

- Autenticación de usuarios
- Base de datos persistente
- Interfaz gráfica
- Pagos en línea
- Notificaciones

---

## 🧱 Arquitectura

El sistema sigue una arquitectura en capas:

- **API Layer (FastAPI):** Maneja las solicitudes HTTP
- **Service Layer:** Contiene la lógica de negocio
- **Data Layer:** Almacenamiento en memoria (diccionario)

### 📊 Diagrama

```mermaid
flowchart TD
    Client[Cliente] --> API[FastAPI]
    API --> Service[Lógica de negocio]
    Service --> DB[(Memoria)]
