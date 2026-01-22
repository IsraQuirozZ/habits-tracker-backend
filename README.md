# Habits Backend 🧠📊

Backend del proyecto **Habits**, una aplicación de seguimiento de hábitos personales.

Este backend expone una **API REST desacoplada**, consumida por:

- Frontend web (React)
- Aplicación móvil Android (Kotlin)

No renderiza vistas HTML ni contiene lógica de presentación.

---

## 🚀 Tecnologías

- **Python 3.10+**
- **FastAPI** – Framework para APIs REST
- **Uvicorn** – Servidor ASGI
- **SQLAlchemy** – ORM
- **SQLite** (inicio) → **PostgreSQL** (producción)
- **Pydantic** – Validación de datos
- **Alembic** – Migraciones de base de datos
- **Pytest** – Testing

---

## 📐 Arquitectura

- API REST basada en JSON
- Backend totalmente desacoplado del frontend
- Preparado para autenticación JWT
- Diseño orientado a crecimiento progresivo

📦 El backend **NO**:

- Renderiza HTML
- Usa plantillas (Jinja2, etc.)
- Depende del frontend

---

## 📁 Estructura del proyecto (propuesta)

```text
backend/
├── app/
│   ├── main.py            # Punto de entrada FastAPI
│   ├── core/              # Configuración, settings, seguridad
│   ├── db/                # Base de datos y sesión
│   ├── models/            # Modelos SQLAlchemy
│   ├── schemas/           # Esquemas Pydantic
│   ├── routers/           # Endpoints / rutas
│   └── services/          # Lógica de negocio
├── alembic/               # Migraciones
├── tests/                 # Tests
├── .env.example           # Variables de entorno de ejemplo
├── requirements.txt
└── README.md
```
