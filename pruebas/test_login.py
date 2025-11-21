from paginas.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)

    login.abrir_web()
    login.iniciar_sesion("Admin", "admin123")
    login.validar_login_exitoso()
