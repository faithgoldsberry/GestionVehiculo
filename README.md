# Aplicación de Gestión de Vehículos

## Descripción del Problema

Para gestionar adecuadamente los repuestos de vehículos, es esencial disponer de información precisa de cada vehículo. En Chile, cada vehículo está identificado por una placa patente, aunque no siempre se dispone de esta información (puede haber casos de vehículos sin placa patente o con múltiples placas). Además de la placa patente, cada vehículo tiene un VIN (Número de Identificación del Vehículo), un número de motor, una cilindrada, un año, una marca, un modelo y una versión, y un dueño actual.

## Objetivo

Crear una pequeña webapp que permita consultar la información de un vehículo a partir de una placa patente o por VIN. El sistema debe permitir que un usuario ingrese una placa patente y obtenga toda la información del vehículo asociado. Si no se encuentra un vehículo con la placa ingresada o por VIN, el sistema debe indicar que no existe un vehículo con esa placa o VIN.

## Aplicación

La API debe incluir los siguientes endpoints:

- **GET /vehicle/search**: Consulta la información del vehículo por placa patente o por número de VIN. La información a entregar debe ser la misma para ambos criterios de búsqueda.

  ### Respuesta del Endpoint GET /vehicle/search

  La respuesta del endpoint `GET /vehicle/search` debe incluir la siguiente información:

  - Placas patentes asociadas si existen
  - VIN
  - Número de motor
  - Cilindrada
  - Año
  - Marca
  - Modelo
  - Versión
  - Dueño

- **POST /vehicle**: Permite agregar un nuevo vehículo al sistema, recibe la información del vehículo y alguna de las placas patentes asociadas al vehículo.

  ### Respuesta del Endpoint POST /vehicle

  La respuesta del endpoint `POST /vehicle` confirma la creación del vehículo.

- **GET /vehicles**: Lista todos los vehículos registrados.

  ### Respuesta del Endpoint GET /vehicles

  La respuesta del endpoint `GET /vehicles` es una lista de vehículos que incluye:

  - VIN
  - Número de motor
  - Cilindrada
  - Año
  - Marca
  - Modelo
  - Versión
  - Dueño

## Documentación de la API

La documentación de la API está disponible aquí: https://docs.google.com/document/d/13vYRumprGwccBot37hlVCoOMgwpa819RPz0EQP17cNI/edit?usp=sharing

La documentación de la API está disponible en el repositorio y el Doc de Google. Esta documentación proporciona información detallada sobre cómo interactuar con los endpoints de la API, incluyendo ejemplos y respuestas esperadas.

## Tecnologías Utilizadas

- **Backend**: Django REST framework
- **Frontend**: Nuxt.js, Vuetify, Vue.js

## Instalación y Configuración

**Backend**:
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/faithgoldsberry/Consulta_Vehiculos.git

2. **Navegar al directorio del backend**:
   ```bash
   cd ConsultaVehiculosAPI

3. **Crear un entorno virtual**:
   ```bash
   python3 -m venv env

4. **Activar el entorno virtual**:
   ```bash
   source env/bin/activate

5. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt

6. **Aplicar migraciones**:
   ```bash
   python manage.py migrate

7. **Cargar datos iniciales**:
   ```bash
   python manage.py loaddata vehiculos/fixtures/datos_iniciales.json

8. **Ejecutar el servidor de desarrollo**:
   ```bash
   python manage.py runserver

**Frontend**:
1. **Navegar al directorio del frontend**:
   ```bash
   cd ConsultaVehiculos

2. **Instalar dependencias**:
   ```bash
   npm install

3. **Ejecutar el servidor de desarrollo**:
   ```bash
   npm run dev
