# 🧪 Reto Final - Entorno Local de Desarrollo

Este repositorio contiene una aplicación web desarrollada en Python con Flask, preparada para ejecutarse en un entorno local mediante Docker y Docker Compose.  
Está diseñada para que cualquier miembro del equipo pueda comenzar rápidamente, ejecutar la app, lanzar los tests y colaborar de forma eficiente.

---

## 📦 Arquitectura del Software

La solución está compuesta por los siguientes componentes:

- **Python 3.10** – Lenguaje principal de desarrollo
- **Flask** – Framework web
- **SQLAlchemy** – ORM para gestionar la base de datos
- **PostgreSQL 15** – Base de datos relacional
- **Docker + Docker Compose** – Contenedores y orquestación
- **Pytest + Coverage** – Testing automatizado con reporte de cobertura

---

## ⚙️ Cómo iniciar el entorno local

### 1. Clona el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <carpeta_del_repo>
```

### 2. Crea un archivo `.env` en la raíz (si no está ya) con este contenido:

```env
FLASK_ENV=development
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=devdb
POSTGRES_PORT=5432
POSTGRES_HOST=db
DATABASE_URI=postgresql://devuser:devpass@db:5432/devdb
```

### 3. Lanza la aplicación y la base de datos:

```bash
docker-compose up --build
```

La aplicación estará disponible en [http://localhost:5000](http://localhost:5000)

---

## 🧪 Cómo ejecutar los tests

```bash
docker-compose run --rm web pytest --cov=app --cov-report=term-missing
```

Este comando ejecuta la batería de tests unitarios y muestra el porcentaje de cobertura.  
Actualmente se garantiza una cobertura **mínima del 80 %**, incluyendo rutas, errores y modelos.

---

## 🧭 Rutas disponibles

- `GET /` → Saludo básico
- `GET /data` → Lista de registros en base de datos
- `POST /data` → Crea un nuevo registro (requiere JSON con clave `"name"`)

---

## 🤝 Normas de colaboración

Modelo de ramas propuesto:

- `main` → Rama de producción estable
- `develop` → Rama de desarrollo integrada
- `feature/<nombre>` → Para cada nueva funcionalidad o mejora

### Reglas:

- Todas las nuevas features se desarrollan en `feature/`
- Toda PR debe ir a `develop`, pasar los tests y mantener la cobertura mínima
- Se recomienda usar `black`, `flake8` o similar para mantener el estilo

---

## ✅ Requisitos cumplidos en este entorno

✔️ Docker y base de datos local funcional  
✔️ Pruebas unitarias con cobertura > 80%  
✔️ App accesible por navegador  
✔️ Documentación para onboarding  
✔️ Configuración reproducible mediante `.env`

---

## 📌 Notas finales

Este entorno está preparado para permitir la incorporación de nuevos miembros de forma rápida, con instrucciones claras y herramientas integradas para testing, despliegue local y desarrollo colaborativo.