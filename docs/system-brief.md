# 🧾 System Brief

## 📌 Nombre del sistema
Sistema de Gestión de Citas Médicas (Appointment API MVP)

---

## ❗ Problema

En muchos entornos de atención médica, especialmente en pequeñas clínicas o procesos manuales, la gestión de citas presenta múltiples problemas:

- Registro manual propenso a errores
- Falta de seguimiento de citas
- Dificultad para consultar información rápidamente
- Procesos poco eficientes y no escalables

Esto afecta tanto a pacientes como al personal administrativo.

---

## 💡 Solución

Se propone una API REST que permite gestionar citas médicas de forma digital, simple y estructurada.

El sistema permite:

- Crear citas médicas
- Consultar citas por ID
- Actualizar el estado de una cita
- Listar todas las citas registradas

Todo a través de endpoints HTTP accesibles.

---

## 👥 Usuarios objetivo

- Personal administrativo de clínicas
- Sistemas externos (frontends o apps móviles)
- Desarrolladores que necesiten integrar gestión de citas

---

## 🎯 Objetivo del MVP

Validar el flujo principal de negocio:

👉 **Registro y seguimiento de citas médicas**

El objetivo es demostrar una API funcional que represente este flujo sin necesidad de implementar todas las características de un sistema completo.

---

## ⚙️ Alcance (Scope)

### ✅ Incluido

- API REST funcional
- Creación de citas
- Consulta por ID
- Listado de citas
- Actualización de estado
- Validación básica de datos

---

### ❌ No incluido

- Autenticación de usuarios
- Base de datos persistente
- Interfaz gráfica
- Pagos o facturación
- Notificaciones (email/SMS)

---

## 🧱 Descripción general del sistema

El sistema está construido bajo una arquitectura simple en capas:

- **API Layer:** Maneja las solicitudes HTTP
- **Service Layer:** Contiene la lógica de negocio
- **Data Layer:** Almacenamiento temporal en memoria

Esto permite una implementación rápida, clara y adecuada para un MVP.

---

## 🚀 Resultado esperado

Un sistema API que:

- Sea ejecutable localmente
- Responda correctamente a solicitudes HTTP
- Permita gestionar citas médicas básicas
- Sirva como base para futuras mejoras

---

## 📌 Estado actual

El sistema corresponde a un MVP funcional que cubre el flujo principal del negocio, listo para pruebas, validación y expansión futura.
