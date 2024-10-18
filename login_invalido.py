import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_login_invalido():
    driver = setup_driver()
    try:
        driver.get("http://localhost:4200/")  # URL da página de login
        
        # Espera alguns segundos para garantir que a página carregou (diagnóstico temporário)
        time.sleep(5)

        # Usa 'name' para localizar o campo de username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys('usuario_nao_existente')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys('senha_qualquer')

        # Clica no botão de "Entrar"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        ).click()

        # Verifica se a mensagem "Não há usuários cadastrados" aparece
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'error-message'), "Não há usuários cadastrados")
        )
        
        time.sleep(5)

    finally:
        driver.quit()

