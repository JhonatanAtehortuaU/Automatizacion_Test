from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators NUEVOS de OrangeHRM
        self.username = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.button_login = (By.XPATH, "//button[@type='submit']")
        self.dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")

    def abrir_web(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
    
    def iniciar_sesion(self, user, password):
        # Esperar campo usuario
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)

        # Esperar campo contraseña
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

        # Click login
        self.wait.until(EC.element_to_be_clickable(self.button_login)).click()

    def validar_login_exitoso(self):
        self.wait.until(EC.visibility_of_element_located(self.dashboard_text))
