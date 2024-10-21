import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_deletar_usuario():
    driver = setup_driver()
    try:
        driver.get("http://localhost:4200/cadastro")  

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'nome'))
        ).send_keys('cobaia')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        ).send_keys('cobaia@example.com')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'senha'))
        ).send_keys('cobaia123')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'home-container'))
        )

        # Verifica se o usuário foi criado e está listado na página
        usuario_cadastrado = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[strong/text()='Nome:']/following-sibling::p[contains(text(), 'cobaia')]"))
        )
        print(f"cobaia: {usuario_cadastrado.text}")

        # Hora de aguarda
        time.sleep(2)

        # Deletar usuario
        botao_deletar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[strong/text()='Nome:']/following-sibling::button[contains(text(), 'Deletar')]"))
        )
        botao_deletar.click()

        # Aguardar denovo
        time.sleep(3)

        # Verifica remoção
        usuario_removido = driver.find_elements(By.XPATH, "//p[strong/text()='Nome:']/following-sibling::p[contains(text(), 'cobaia')]")

        # Se a lista estiver vazia = CPF cancelado
        assert len(usuario_removido) == 0, "O usuário ainda está na lista."

        print("Teste passou: CPF cancelado.")

    except Exception as e:
        print(f"Falhou!!! erro: {e}")

    finally:
        driver.quit()

