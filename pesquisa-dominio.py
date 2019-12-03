from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def run():
    print("Iniciando automação...\n")

    lista_salva = open('resultado.txt', 'w')

    driver = webdriver.Chrome('/home/whoami/curso-python/curso-udemy/bot/chromedriver_77')

    driver.get('https://registro.br/')

    dominios = ['roboscompython.com.br', 'udemy.com', 'uol.com.br', 'pythoncurso.com']

    for dominio in dominios:
        pesquisa = driver.find_element_by_id('is-avail-field')
        pesquisa.clear()
        
        pesquisa.send_keys(dominio)
        pesquisa.send_keys(Keys.RETURN)
        
        time.sleep(1) #esperando renderizar a página

        resultado = driver.find_element_by_css_selector('p.font-3 strong')

        texto = "Domínio {} {}\n". format(dominio, resultado.text)
        
        print(texto)
        
        lista_salva.write(texto)


    lista_salva.close()

    print("#####################")
    print("Finalizando...")

    time.sleep(2)
    driver.close()


if __name__ == "__main__":
    run()
