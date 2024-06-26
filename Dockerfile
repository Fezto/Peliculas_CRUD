FROM python:3.12.3
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["flask", "run"]