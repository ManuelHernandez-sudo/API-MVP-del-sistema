# 🏗️ Architecture

## 📌 Descripción general

El sistema **Sistema de Gestión de Citas Médicas (MVP)** está diseñado utilizando una arquitectura en capas (Layered Architecture), con el objetivo de mantener separación de responsabilidades, simplicidad y facilidad de evolución.

Esta arquitectura permite escalar el sistema en el futuro sin afectar significativamente los componentes existentes.

---

## 🧱 Componentes principales

### 🔹 API Layer (FastAPI)

Responsabilidades:

- Exponer endpoints HTTP
- Recibir y validar requests (Pydantic)
- Manejar respuestas y códigos de estado
- Conectar con la capa de servicios

---

### 🔹 Service Layer

Responsabilidades:

- Implementar la lógica de negocio
- Gestionar reglas del sistema
- Procesar operaciones sobre citas
- Servir como intermediario entre API y datos

---

### 🔹 Data Layer

Responsabilidades:

- Almacenamiento de datos en memoria (diccionario)
- Persistencia temporal durante ejecución
- Simulación de base de datos

---

## 📊 Diagrama de arquitectura

```mermaid
flowchart TD
    Client[Cliente / Usuario] --> API[FastAPI API]
    API --> Service[Lógica de negocio]
    Service --> DB[(Almacenamiento en memoria)]
