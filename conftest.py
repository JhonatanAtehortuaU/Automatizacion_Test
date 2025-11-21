import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()

    # Si quieres que no se vea la ventana, quita el comentario:
    # options.add_argument("--headless")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.maximize_window()

    yield driver
    driver.quit()
