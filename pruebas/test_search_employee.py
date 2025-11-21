from paginas.login_page import LoginPage
from paginas.pim_page import PIMPage

def test_buscar_empleado(driver):
    login = LoginPage(driver)
    login.abrir_web()
    login.iniciar_sesion("Admin", "admin123")

    pim = PIMPage(driver)
    pim.ir_a_pim()
    pim.buscar_empleado("0345")  # Cambia por un ID real existente
