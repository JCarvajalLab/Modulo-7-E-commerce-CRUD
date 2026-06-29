# ACCESO A DATOS EN APLICACIONES PYTHON DJANGO (V2)
##  Tabla de contenidos

- [ACCESO A DATOS EN APLICACIONES PYTHON DJANGO (V2)](#acceso-a-datos-en-aplicaciones-python-django-v2)
- [Tabla de contenidos](#tabla-de-contenidos)
- [Instrucciones](#instrucciones)
- [Construido con](#construido-con)
- [Descripción del modelo de datos](#descripción-del-modelo-de-datos)
- [Rutas principales del módulo](#rutas-principales-del-módulo)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Evidencia](#evidencia)
- [Repositorio](#repositorio)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Autor](#autor)

## Instrucciones

Implementar la capa de acceso a datos del e-commerce utilizando Django y su ORM,
permitiendo administrar el catálogo de productos mediante operaciones CRUD, integrando
modelos, relaciones, migraciones y consultas, dentro de una aplicación web basada en el
patrón MVC de Django.

## Construido con

- Python 3.x — Lenguaje base del proyecto
- PostgreSQL — Motor de base de datos relacional
- Django 6.0.6 — Framework web y ORM
- psycopg2-binary 2.9.12 — Adaptador PostgreSQL para Python

## Descripción del modelo de datos
### Categoria

| Campo    | Tipo        | Descripción                        |
|----------|-------------|-------------------------------------|
| `id`     | BigAutoField | Clave primaria (automática)        |
| `nombre` | CharField | Nombre único de la categoría     |

### Producto

| Campo           | Tipo              | Descripción                              |
|-----------------|-------------------|-------------------------------------------|
| `id`            | BigAutoField      | Clave primaria (automática)              |
| `nombre`        | CharField         | Nombre del producto                      |
| `descripcion`   | TextField         | Descripción detallada                    |
| `precio`        | DecimalField      | Precio con hasta 10 dígitos y 2 decimales |
| `stock`         | PositiveIntegerField | Cantidad disponible (mínimo 0)        |
| `categoria`     | ForeignKey        | Relación con Categoria (PROTECT)         |
| `creado_en`     | DateTimeField     | Fecha de creación (automática)           |
| `actualizado_en`| DateTimeField     | Fecha de última edición (automática)     |

## Rutas principales del módulo

 Ruta                        | Vista               | Descripción              |
-----------------------------|---------------------|--------------------------|
 `/productos/`               | lista_productos   | Listado de productos     |
 `/productos/crear/`       | crear_producto    | Formulario de creación   |
 `/productos/editar/<id>/` | editar_producto   | Formulario de edición    |
 `/productos/eliminar/<id>/` | eliminar_producto | Confirmación y eliminación |
`/admin/`                   | Django Admin        | Panel administrativo     |

## Instalación y ejecución
### Prerrequisitos

- Python 3.10 o superior
- PostgreSQL instalado y en ejecución
- pip

### 1. Clonar el repositorio

```bash
git clone https://github.com/JCarvajalLab/Modulo-7-E-commerce-CRUD.git
cd Modulo-7-E-commerce-CRUD
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crea la base de datos y el usuario en PostgreSQL:

```sql
CREATE DATABASE gamer_store_db;
CREATE USER gamer_store_user WITH PASSWORD 'gamer1234';
GRANT ALL PRIVILEGES ON DATABASE gamer_store_db TO gamer_store_user;
```

Conectar base de datos a `settings.py`

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gamer_store_db",
        "USER": "gamer_store_user",
        "PASSWORD": "gamer1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 5. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario (para acceder al admin)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Accede a la aplicación en [http://127.0.0.1:8000/productos/](http://127.0.0.1:8000/productos/)
Panel admin en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Evidencia
### Listado de productos
![alt text](/static/images/image.png)
### Formulario de creación
![alt text](/static/images/image-1.png)
### Formulario de edición
![alt text](/static/images/image-2.png)
### Confirmación de eliminación
![alt text](/static/images/image-3.png)
### Alerta de edicion realizada
![alt text](/static/images/image-4.png)
### Panel administrativo
![alt text](/static/images/image-5.png)

![alt text](/static/images/image-6.png)

![alt text](/static/images/image-7.png)

![alt text](/static/images/image-8.png)

### PostgreSQL
![alt text](/static/images/image-9.png)

![alt text](/static/images/image-10.png)

![alt text](/static/images/image-11.png)
## Repositorio

🔗 [https://github.com/JCarvajalLab/Modulo-7-E-commerce-CRUD](https://github.com/JCarvajalLab/Modulo-7-E-commerce-CRUD)

---

## Estructura del proyecto

```
└── 📁ecommerce
    └── 📁config
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
    └── 📁productos
        └── 📁migrations
            ├── __init__.py
            ├── 0001_initial.py
            ├── 0002_alter_categoria_options_producto.py
        └── 📁templates
            └── 📁productos
                ├── crear_producto.html
                ├── editar_producto.html
                ├── eliminar_producto.html
                ├── lista_productos.html
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    └── 📁static
        └── 📁css
            ├── styles.css
        └── 📁images
        └── 📁js
    └── 📁templates
        └── 📁includes
            ├── footer.html
            ├── navbar.html
        ├── base.html
    ├── manage.py
    ├── README.md
    └── requirements.txt
```
## Autor

**Actividad Final - Modulo 7 - Desarrollo Portafolio**

**Alumno:** Jordan Carvajal - **Fecha:** 28-06-2026

