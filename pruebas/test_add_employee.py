from paginas.login_page import LoginPage
from paginas.pim_page import PIMPage

def test_crear_empleado(driver):
    login = LoginPage(driver)
    login.abrir_web()
    login.iniciar_sesion("Admin", "admin123")

    pim = PIMPage(driver)
    pim.ir_a_pim()
    pim.ir_agregar_empleado()
    pim.crear_empleado("Juan", "Perez")
