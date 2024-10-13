import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def scraping_process(domains_tld_for_search):
    """
    Obtengo los dominios de la fuente
    
    Returns: 
        Lista de dominios obtenidos mediante scraping
    """
    
    # inicio chrome con la página de donde "rascar" la información
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://dnpedia.com/domains/dailydata.php")
    time.sleep(4)

    
    # le mando al input, relacionado con el tld, la información a buscar 
    tld_input = driver.find_element(By.ID, "zone-tld-selection")
    tld_input.send_keys(domains_tld_for_search)
    time.sleep(7)

    # hago click para que nos muestre la información
    driver.find_element(By.ID, "btn-find-added-domains").click()
    time.sleep(6)

    # recorro los elementos donde se encuentran los valores de los dominios
    # domains_list = driver.find_elements(By.CSS_SELECTOR, "#domaindata > ul > li")
    # for domain in domains_list:
    #     print(domain.text)
    
    # también se pueden obtener los dominios con beatiful soup
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    # domains_values = soup.find(id='domaindata').find('ul').find_all('li')
    # for domain in domains_values:
    #     print(domain.text)
        
    domains_list = driver.find_elements(By.CSS_SELECTOR, "#domaindata > ul > li")
    
    return domains_list


def get_domains(scraped_list):
    """Devuelvo la lista directamente de dominios

    Args:
        scraped_list (list): lista de dominios scrapeados

    Returns: 
        lista de dominios utilizable
    """
    domains = []
    for domain in scraped_list:
        domains.append(domain.text)
        
    return domains


if __name__ == "__main__":
    # scraping_process('tech')
    # print(get_domains(scraping_process('biz')))
    print(get_domains(scraping_process('online')))
