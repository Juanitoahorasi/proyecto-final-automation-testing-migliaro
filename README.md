Autor: Juan Migliaro
Curso: Automatización QA
Tecnologías: Python, Pytest, Selenium, Requests

Descripción del proyecto

Este proyecto implementa un framework de automatización de pruebas UI y API utilizando únicamente herramientas vistas en el curso.
El objetivo es demostrar un flujo de automatización completo, ordenado, simple y extensible.

Incluye:

Pruebas UI en https://www.saucedemo.com

Pruebas API en JSONPlaceholder

Page Object Model (POM)

Capturas automáticas de pantalla en fallos

Reportes HTML

Logging centralizado




Estructura del proyecto :

proyecto-final-automation-testing-migliaro/
├── config/
│ └── settings.py
├── pages/
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ ├── checkout_information_page.py
│ ├── checkout_overview_page.py
│ └── checkout_complete_page.py
├── tests/
│ ├── ui/
│ │ ├── test_login.py
│ │ ├── test_add_to_cart.py
│ │ └── test_checkout.py
│ └── api/
│ ├── test_get_posts.py
│ ├── test_create_post.py
│ └── test_delete_post.py
├── utils/
│ ├── driver_factory.py
│ ├── logger.py
│ ├── screenshot.py
│ └── api_client.py
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
└── README.md

Para correr las pruebas del proyecto

Instalar dependencias:

pip install -r requirements.txt


Ejecutar solo las pruebas UI:

pytest -m ui --html=reports/ui_report.html --self-contained-html


Ejecutar solo las pruebas API:

pytest -m api --html=reports/api_report.html --self-contained-html


Ejecutar todas las pruebas del framework:

pytest --html=reports/full_report.html --self-contained-html


Los reportes HTML generados aparecerán dentro de la carpeta:

/reports


Las capturas de pantalla en caso de errores aparecerán en:

/screenshots



Instalación y configuración

Clonar el repositorio:

git clone https://github.com/juanitoahorasi/proyecto-final-automation-testing-migliaro.git

cd proyecto-final-automation-testing-migliaro

Crear entorno virtual (opcional):

python -m venv venv
venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt






Requisitos:

Microsoft Edge instalado

msedgedriver accesible en PATH

Ejecución de pruebas
Ejecutar solo UI

pytest -m ui --html=reports/ui_report.html --self-contained-html

Ejecutar solo API

pytest -m api --html=reports/api_report.html --self-contained-html

Ejecutar todo el test suite

pytest --html=reports/full_report.html --self-contained-html

Capturas automáticas

Cuando un test UI falla, se genera automáticamente una captura con timestamp en:

/screenshots/

El reporte HTML muestra un link al archivo generado.

Page Object Model (POM)

Páginas implementadas:

LoginPage

InventoryPage

CartPage

CheckoutInformationPage

CheckoutOverviewPage

CheckoutCompletePage

Cada página encapsula localizadores, acciones del usuario y métodos de validación.

Pruebas de API

Implementadas con requests y ApiClient.

Endpoints utilizados:

GET /posts → validación de estructura JSON

POST /posts → simulación de creación

DELETE /posts/1 → simulación de eliminación

Logging

El archivo utils/logger.py crea un logger global:

Log en test_execution.log

Output también en consola

Reportes HTML

Los reportes se generan con pytest-html y se guardan en:

/reports/

Abrilos con cualquier navegador.

Integración Continua (GitHub Actions)

Incluye workflow simple que ejecuta las pruebas automáticamente al hacer push.

Archivo:

.github/workflows/python-tests.yml

Mejoras opcionales

Parametrización con JSON/CSV

CI/CD completo con ejecución de UI en headless mode

Data loader para pruebas dinámicas

Autor

Juan Migliaro
Proyecto Final – Automatización QA