# DJANGO LMS 
_Sistema de gestión de aprendizaje._

## Pasos para la instalación
_Estas instrucciones te permitirán obtener una copia del proyecto en 
funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋
- Tener instalado [Python 3.7](https://www.python.org/downloads/release/python-370/)
y un entorno virtual con el mismo.

### Instalación 🔧
- Activar su entorno virtual e instalar los requerimientos:
   ```
    pip install -r requirements.txt
    ```
- Hacer las migraciones:
    ```
    python manage.py makemigrations
    ```
   ```
   python manage.py migrate
   ``` 

- Crear un superusuario
    ```
     python manage.py createsuperuser --username admin
    ```
  
- Correr el proyecto localmente
    ```
    python manage.py runserver
    ```  
 ## Wiki 📖
 Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/django-lms/LMS/wiki)

## Autores ✒️
_Espacio reservado para los genios._

## Licencia 📄
Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles.