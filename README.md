🚀 Automatización de Pruebas – OrangeHRM
📌 Descripción del proyecto

Este proyecto consiste en la automatización de 3 funcionalidades críticas del sistema OrangeHRM Demo, utilizando Python + Selenium + Pytest, aplicando buenas prácticas como Page Object Model (POM) y técnicas de optimización para mejorar estabilidad y mantenibilidad.

Sistema probado

URL: https://opensource-demo.orangehrmlive.com/
Usuario: Admin
Contraseña: admin123

🎯 Funcionalidades automatizadas

✅ Login exitoso

✅ Creación de empleado

✅ Búsqueda de empleado


orangehrm_automation/
│
├── paginas/
│   ├── login_page.py
│   └── pim_page.py
│
├── pruebas/
│   ├── test_login.py
│   ├── test_add_employee.py
│   └── test_search_employee.py
│
├── conftest.py
└── requirements.txt
______________________________________________________________________________________________________________________________________________________________________________________

⚙️ Instalación
Instalar dependencias

Instalar Firefox

Primero revisa si ya lo tienes:
firefox --version

Si no está instalado:

En Ubuntu / Debian:
sudo apt update
sudo apt install firefox

Instalar GeckoDriver

Firefox usa un driver llamado GeckoDriver.

En terminal:
sudo apt install firefox-geckodriver

Verifica que funcione:
geckodriver --version

Ubícate en la raíz del proyecto y ejecuta:
pip install -r requirements.txt

______________________________________________________________________________________________________________________________________________________________________________________

ejecución de los tests

Para ejecutar todas las pruebas:
pytest -v

Para ejecutar una prueba específica:
pytest tests/test_login.py -v

Descripción de los tests
🔹 test_login.py

Valida que el usuario Admin pueda iniciar sesión correctamente.

🔹 test_add_employee.py

Valida que se pueda crear un nuevo empleado dentro del sistema.

🔹 test_search_employee.py

______________________________________________________________________________________________________________________________________________________________________________________

Valida que se puede buscar un empleado existente.

Proceso de optimización aplicado

Se aplicaron las siguientes optimizaciones:

✅ Uso de Page Object Model (POM)
✅ Eliminación de repetición de código
✅ Optimización de selectores XPath
✅ Organización por módulos
✅ Preparación para escalabilidad futura
✅ Sustitución futura de time.sleep() por WebDriverWait



