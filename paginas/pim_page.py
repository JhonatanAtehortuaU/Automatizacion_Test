from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators corregidos
        self.menu_pim = (By.XPATH, "//span[text()='PIM']/ancestor::a")

        self.btn_add = (By.XPATH, "//button[normalize-space()='Add']")
        self.input_firstname = (By.NAME, "firstName")
        self.input_lastname = (By.NAME, "lastName")
        self.btn_save = (By.XPATH, "//button[@type='submit']")

        self.emp_id_field = (By.XPATH, "//label[text()='Employee Id']/following::div/input")

    def ir_a_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_pim)).click()

    def ir_agregar_empleado(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_add)).click()

    def crear_empleado(self, nombre, apellido):
        self.wait.until(EC.visibility_of_element_located(self.input_firstname)).send_keys(nombre)
        self.wait.until(EC.visibility_of_element_located(self.input_lastname)).send_keys(apellido)
        self.wait.until(EC.element_to_be_clickable(self.btn_save)).click()

    def buscar_empleado(self, emp_id):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List"))).click()

        input_id = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Employee Id']/following::input[1]"))
        )

        input_id.send_keys(emp_id)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))
        ).click()
