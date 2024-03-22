from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable='chromedriver')

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser

if __name__ == '__main__':
    options = ()
    browser = make_chrome_browser(*options)

    # Navega até a página
    browser.get('https://demo.guru99.com/test/simple_context_menu.html')

    # Espera 2 segundos para garantir que a página tenha carregado completamente
    sleep(10)

    # Fecha o navegador
    browser.quit()
