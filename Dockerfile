# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el contenido del directorio actual al contenedor
COPY . /app

# Instala las dependencias
RUN pip install flask mysql-connector-python

# Expone el puerto que la app usa
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
