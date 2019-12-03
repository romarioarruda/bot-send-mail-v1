from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# email = input('Digite seu e-mail: \n')
# senha = input('Digite sua senha: \n')
email = 'exemplo@gmail.com'
senha = 'senha'

assunto = 'E-mail enviado pelo bot'
mensagem = 'Esta mensagem é um teste realizado com um software de automação.'
  

def run():
    print("Iniciando execução do bot...\n")
    driver = webdriver.Chrome('/home/whoami/curso-python/curso-udemy/bot/chromedriver_77')
    
    print("Abrindo o Gmail...\n")
    driver.get('https://www.google.com/gmail/')

    #LOGIN
    print("Realizando login...\n")
    input_email = driver.find_element_by_id('identifierId')
    input_email.clear()

    input_email.send_keys(email)
    input_email.send_keys(Keys.RETURN)
    time.sleep(2)
    #SENHA
    input_senha = driver.find_element_by_name('password')
    input_senha.clear()

    input_senha.send_keys(senha)
    input_senha.send_keys(Keys.RETURN)
    time.sleep(10)
    print("Login realizado!\n")

    print("Abrindo caixa de e-mail..\n")
    driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    time.sleep(6)

    print("Informando destinatário..\n")
    destino = driver.find_element_by_name('to')
    destino.send_keys(email)
    destino.send_keys(Keys.RETURN)

    print("Informando assunto do e-mail..\n")
    subject = driver.find_element_by_name('subjectbox')
    subject.send_keys(assunto)
    subject.send_keys(Keys.RETURN)

    print("Escrevendo a mensagem do e-mail..\n")
    corpo_msg = driver.find_element_by_xpath('//div[@aria-label="Corpo da mensagem"]')
    corpo_msg.clear()
    corpo_msg.send_keys(mensagem)

    print("Enviando e-mail..\n")
    btn_env = driver.find_element_by_xpath('//div[@aria-label="Enviar ‪(Ctrl-Enter)‬"]')
    btn_env.click()
    time.sleep(5)

    print("E-mail enviado, vou deslogar...\n")

    driver.get('https://accounts.google.com/Logout')

    print("Deslogado! Fechando o navegador...\n")
    time.sleep(3)
    driver.close()


if __name__ == "__main__":
    run()
