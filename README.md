# Deployment

Para ejecutar el servidor localmente, sigue estos pasos:

1. Clona el repositorio:

    ```
    git clone git@github.com:fedemarkco/Entelai.git
    ```

2. Cambia al directorio del proyecto:

    ```
    cd Entelai
    ```

3. Crea y activa un entorno virtual:

    ```
    python3 -m venv project
    source project/bin/activate
    ```

4. Instala las dependencias:

    ```
    pip install -r requirements.txt
    ```

5. Ejecuta el servidor:

    ```
    python3 manage.py runserver
    ```

# Endpoints

Ambos endpoints utilizan el método POST.

- Para iniciar el proyecto:

    ```
    http://localhost:5000/start
    ```

- Para elegir una opción, envía un JSON en el cuerpo de la solicitud:

    ```
    http://localhost:5000/choose
    ```

    ```
    {
        "node_id": int
    }
    ```

# Capturas de pantalla

Puedes encontrar capturas de pantalla de cómo ejecutar las solicitudes en Postman en la carpeta `Postman`.

# Testing

Para ejecutar los tests, utiliza el siguiente comando:

```
python -m unittest app.tests.test_node
```

Autor: Marco Weihmüller
