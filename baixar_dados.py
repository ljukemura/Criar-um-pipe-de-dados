from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


navegador.get('https://www.kaggle.com/datasets/anasmahmood000/coursera-courses-dataset')
navegador.find_element('xpath',
                       '//*[@id="site-content"]/div[2]/div[2]/div/div[1]/div/a/button/span').click()

navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div/div[2]/a/li/div/span').click()

time.sleep(3)

navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div[1]/div/label/input').send_keys('testeljukemura@gmail.com')
navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div[2]/div/label/input').send_keys('testeljuke')

time.sleep(3)

navegador.find_element('xpath',
                       '//*[@id="site-container"]/div/div[2]/form/div[2]/div[3]/button/span').click()

time.sleep(3)
navegador.find_element('xpath',
                       '//*[@id="site-content"]/div[2]/div[2]/div/div[1]/div/a/button/span').click()
time.sleep(10)

