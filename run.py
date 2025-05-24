import time
import psycopg2
import os
from app import create_app, db
from app.models import Data

# Esperar a que PostgreSQL esté disponible
while True:
    try:
        conn = psycopg2.connect(
            host="db",
            database="devdb",
            user="devuser",
            password="devpass"
        )
        conn.close()
        break
    except psycopg2.OperationalError:
        print("Esperando a que la base de datos esté lista...")
        time.sleep(1)

# Obtener entorno desde variable
env = os.getenv("FLASK_ENV", "development")
app = create_app(env)

# Crear tablas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
