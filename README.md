
# 🧾 API Gestión de Inventario

API RESTful construida en Flask que permite gestionar usuarios, productos, categorías, órdenes, reportes y proveedores en un sistema de inventario.

---

## 🌐 Base URL

- Desarrollo: `http://localhost:5010`
- Producción: *(Por definir)*

---

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Flask
- Flask-Cors
- mysql-connector-python
- PyJWT
- Pillow
- python-dotenv
- Graphviz + Pyreverse
- Visual Studio Code

---

## 🔐 Autenticación

Se requiere token para acceder a la mayoría de los endpoints.

### ➕ Login

```bash
POST /login
Authorization: Basic <username:password>
```

**Respuesta:**

```json
{
  "token": "tu-token-aqui",
  "username": "usuario",
  "id": 1
}
```

Agrega el token en las siguientes solicitudes con el header:

```
x-access-token: tu-token-aqui
```

---

## 📌 Endpoints principales

### 👤 Usuarios

**Registrar:**

```http
POST /register
```

```json
{
  "username": "usuario",
  "password": "clave"
}
```

---

### 👥 Personas

**Obtener todas:**

```http
GET /persons
```

**Crear:**

```http
POST /persons
```

```json
{
  "name": "Carlos",
  "surname": "Gómez",
  "email": "carlos@mail.com",
  "dni": 56778899
}
```

---

### 📦 Productos

**Actualizar stock:**

```http
PUT /user/<id_user>/product/<id_product>/stock
```

```json
{
  "quantity": 10
}
```

**Eliminar producto:**

```http
DELETE /user/<id_user>/product/<id_product>
```

---

## ❌ Errores comunes

- `401 Unauthorized`: Token inválido o faltante.
- `404 Not Found`: Recurso no encontrado.
- `500 Internal Server Error`: Fallo del servidor.

---

## 📥 Pruebas con Postman

Colección disponible:  
[Descargar desde GitHub](https://github.com/Criistian91/inventory_project_proyectoinfor/blob/back/inventory-management-system/api/tests/Gesti%C3%B3n%20de%20inventario%20API.postman_collection.json)

---

## 🧰 Generación de Diagramas UML

### Requisitos

- Entorno virtual activado
- Pyreverse (`pylint`) instalado
- Graphviz instalado y agregado al PATH

### Comandos

Desde la carpeta `api/`:

```bash
pyreverse -o png -p backend_diagrama models routes utils
```

### Archivos generados

- `classes_backend_diagrama.png`
- `packages_backend_diagrama.png`

---

## 📁 Estructura del backend

```bash
api/
├── models/           # Clases y lógica de negocio
├── routes/           # Rutas/endpoints
├── utils/            # Seguridad y manejo de errores
├── db/               # Configuración base de datos
├── __init__.py       # Punto de entrada Flask
└── README.md         # Este archivo
```

---

## 👨‍💻 Autores

- Cristian – Backend
- Daniel – Frontend

Proyecto Informático – Año 2025
