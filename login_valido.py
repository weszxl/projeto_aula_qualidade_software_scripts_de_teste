import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_login_valido():
    driver = setup_driver()
    try:
        driver.get("http://localhost:4200/")  # URL da página de login

        # Espera alguns segundos para garantir que a página carregou
        time.sleep(5)

        # Usa 'name' para localizar o campo de username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys('usuario_teste')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys('senha_teste')

        # Clica no botão de "Entrar"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        ).click()

        # Aumenta o tempo de espera se necessário
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'success-message'))  # Localize o elemento que contém a mensagem de sucesso
        )

        # Verifica se a mensagem de sucesso aparece
        success_message = driver.find_element(By.ID, 'success-message').text
        assert "Login efetuado com sucesso" in success_message

    finally:
        driver.quit()
