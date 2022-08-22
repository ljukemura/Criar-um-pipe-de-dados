from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

email = 'testeljukemura@gmail.com'
with open('senha.txt', 'r') as a:
    senha = a.read()


#abre o site
navegador.get('https://www.kaggle.com/datasets/anasmahmood000/coursera-courses-dataset')

#clica no botão de download
navegador.find_element('xpath',
                       '//*[@id="site-content"]/div[2]/div[2]/div/div[1]/div/a/button/span').click()

#escolhe opção para entrar via e-mail
navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div/div[2]/a/li/div/span').click()

#dar um tempinho para carregar e preenche os dados
time.sleep(1)
navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div[1]/div/label/input').send_keys(email)
navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div[2]/div/label/input').send_keys(senha)

#aperta botão confirmar
time.sleep(1)
navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div[3]/button/span').click()

time.sleep(3)
#clica no botão de download
navegador.find_element('xpath',
                       '//*[@id="site-content"]/div[2]/div[2]/div/div[1]/div/a/button/span').click()
time.sleep(5)

