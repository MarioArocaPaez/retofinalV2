# Bloque 3: Infraestructura como Código (IaC)

## ✅ Enfoque elegido

Se ha optado por utilizar Terraform junto con el proveedor `kreuzwerker/docker` para definir y desplegar la infraestructura de la aplicación **de forma totalmente local**, sin necesidad de una cuenta en AWS u otros servicios cloud.

Este enfoque permite:
- Reproducir el entorno sin depender de la nube
- Ejecutar infraestructura en máquinas locales (desarrollo o pruebas)
- Cumplir con los principios de Infraestructura como Código (IaC)

## 🧱 Infraestructura definida

- Red Docker: `reto-network`
- Contenedor Docker: `reto-final-container`
- Imagen usada: `nginx` (por defecto)
- Puerto mapeado: `localhost:5000` → `container:80`

## 📂 Estructura de archivos

```
infra/
├── main.tf              # Configuración principal de Terraform
├── variables.tf         # Variables reutilizables
├── terraform.tfvars     # Valores de las variables para esta ejecución
├── .terraform.lock.hcl  # Archivo generado tras 'terraform init'
```

## ⚙️ Uso

Desde el directorio `infra/`, ejecutar:

```bash
terraform init
terraform apply
```

Esto creará automáticamente:
- Una red Docker llamada `reto-network`
- Un contenedor con la imagen especificada y puerto 5000 expuesto

## 🌍 Acceso a la aplicación

Una vez ejecutado, puedes acceder desde el navegador a:

```
http://localhost:5000
```

## 🔧 Personalización

Puedes cambiar la imagen Docker en `terraform.tfvars`:

```hcl
docker_image = "nginx"
```

También puedes modificar el nombre del contenedor o los puertos en `main.tf`.

## 📝 Justificación

Dado que el reto permite usar cualquier tecnología que cumpla con los objetivos del bloque 3, y no se exige un entorno cloud específico, se justifica esta decisión porque:
- Permite validación rápida y local
- No requiere credenciales ni configuración de cuentas
- Facilita la evaluación y la corrección