from pathlib import Path
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = os.path.join(ROOT_FOLDER, 'drivers', 'chromedriver')


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Navegar para a página do WhatsApp
    browser.get('https://web.whatsapp.com/')

    # Aguardar até que o elemento do QRCode seja visível na tela
    wait = WebDriverWait(browser, 60)  # ajuste o tempo máximo de espera conforme necessário
    qrcode_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')))

    # Adicionar o restante do código aqui, após o carregamento do QRCode
    # Exemplo:
    # realizar_login(browser)
    # enviar_mensagem(browser, "Olá, mundo!")

    # Manter o programa em execução
    while True:
        sleep(5)
        # Adicionar outras tarefas aqui, se necessário
