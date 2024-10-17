from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver (usando Chrome como exemplo)
def setup_driver():
    driver = webdriver.Chrome()  # Ou o caminho completo se necessário
    driver.implicitly_wait(5)
    return driver

# Função para encerrar o WebDriver
def close_driver(driver):
    driver.quit()
