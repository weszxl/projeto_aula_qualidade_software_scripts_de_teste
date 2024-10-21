import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_senha_curta():
    driver = setup_driver()
    try:
        driver.get("http://localhost:4200/cadastro")  # URL da página de cadastro

        # Espera alguns segundos para garantir que a página carregou
        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'nome'))
        ).send_keys('Charlingtonglaevionbeecheknavare dos Anjos Mendonça Jr')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        ).send_keys('chacha@exemplo.com')

        # Senha com menos de 6 caracteres
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'senha'))
        ).send_keys('123')

        # Verifica se o botão está desabilitado
        botao_cadastrar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )

        # Botão continua desabilitado? (deveria estar)
        assert not botao_cadastrar.is_enabled(), "O botão não está desabilitado."

        print("Teste passou: O botão está desabilitado com um e-mail inválido.")

        time.sleep(5)

    finally:
        driver.quit()

