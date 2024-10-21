import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_criar_usuario():
    driver = setup_driver()
    try:
        driver.get("http://localhost:4200/cadastro")  # URL da página de cadastro

        # Espera alguns segundos para garantir que a página carregou
        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'nome'))
        ).send_keys('agrvai')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        ).send_keys('novousuario@exemplo.com')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'senha'))
        ).send_keys('senha123')

        # Envia formulário "Cadastrar"
        botao_cadastrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        botao_cadastrar.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'home-container'))
        )

        # Verifica mensagem na página
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'success-message'))
        )
        print(f"Mensagem de sucesso: {success_message.text}")

        # Verifica se o nome do usuário aparece na tela
        usuario_cadastrado = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[strong/text()='Nome:']/following-sibling::p[contains(text(), 'agrvai')]"))
        )
        
        assert "agrvai" in usuario_cadastrado.text, "O nome do usuário não aparece na tela."

        print("Teste passou: O nome do usuário aparece.")

        time.sleep(5)

    except Exception as e:
        print(f"Falha!!! erro: {e}")

    finally:
        driver.quit()



