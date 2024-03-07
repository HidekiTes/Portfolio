from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

# Definindo o contato e a mensagem
contact = "Bloco de Notas"
text = "Hey, this message was sent using Selenium"

# Inicializando o driver do Chrome
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Aguardando a entrada do usuário para escanear o código QR
print("Scan QR Code, And then Enter")
input()

# Informando que o usuário está logado
print("Logged In")

try:
    # Localizando o campo de pesquisa e digitando o nome do contato
    search_input_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div'
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, search_input_xpath))
    )
    search_input.click()
    time.sleep(2)
    search_input.send_keys(contact)
    time.sleep(2)

    # Selecionando o contato desejado
    selected_contact_css = f'span[title="{contact}"]'
    selected_contact = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selected_contact_css)))
    selected_contact.click()

    # Localizando o campo de mensagem e enviando a mensagem
    message_input_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div'
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, message_input_xpath))
    )
    time.sleep(2)
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(2)

except TimeoutException:
    print("TimeoutException: Não foi possível encontrar o elemento dentro do tempo limite.")

  
