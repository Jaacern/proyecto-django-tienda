# 🛒 Aplicación Web de Bicicletas con Django - Panel Admin, Registro de Usuarios y Carrito de Compras

Este proyecto es una **aplicación web** creada con Django que permite a los usuarios registrarse, navegar por un catálogo de productos, agregar productos a un carrito de compras y realizar pedidos. Además, cuenta con un panel de administración donde se pueden gestionar productos, usuarios y pedidos.

---

## 📋 Características

- **Panel de administración**: Interfaz de Django para gestionar productos, usuarios y pedidos.
- **Registro de usuarios**: Autenticación y autorización de usuarios.
- **Carrito de compras**: Funcionalidad para agregar, eliminar y visualizar productos en el carrito.
- **Catálogo de productos**: Visualización de productos con detalles.
- **Gestión de pedidos**: Visualización y actualización de pedidos realizados.

---


---

## 🚀 Instalación y Configuración

1. **Clona este repositorio**:
    ```bash
    git clone https://github.com/usuario/proyecto-django-tienda.git
    ```
2. **Navega al directorio del proyecto**:
    ```bash
    cd proyecto-django-tienda
    ```
3. **Crea un entorno virtual** e instálalo:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Para Mac/Linux
    venv\Scripts\activate      # Para Windows
    ```
4. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Realiza las migraciones de la base de datos**:
    ```bash
    python manage.py migrate
    ```

6. **Crea un superusuario** para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```

7. **Ejecuta el servidor**:
    ```bash
    python manage.py runserver
    ```
8. Accede a la aplicación en `http://localhost:8000`.

---

## 🔑 Funcionalidades Principales

### Panel de Administración

Accede al panel de administración de Django en `http://localhost:8000/admin` con el superusuario creado en el paso anterior. Desde aquí podrás gestionar productos, usuarios y pedidos.

### Registro de Usuarios

- Los nuevos usuarios pueden registrarse en la página de registro (`/registro`).
- Los usuarios registrados pueden iniciar sesión para acceder a su perfil, ver su carrito de compras y realizar pedidos.

### Carrito de Compras

- Los usuarios pueden agregar productos al carrito desde el catálogo de productos.
- El carrito muestra los productos seleccionados, permite actualizar cantidades y eliminar elementos.
- Los usuarios pueden proceder al pago desde el carrito.

### Catálogo de Productos

- Página donde se listan todos los productos disponibles con su nombre, imagen y precio.
- Los usuarios pueden hacer clic en cada producto para ver sus detalles y añadirlos al carrito.

---

## 🛠️ Requisitos

- Python 3.6+
- Django 3.2+
- Otros paquetes listados en `requirements.txt`

Instala todas las dependencias con:
```bash
pip install -r requirements.txt
```
📝 Configuración de Variables de Entorno
Crea un archivo .env en la raíz del proyecto y agrega las siguientes variables de entorno:
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

