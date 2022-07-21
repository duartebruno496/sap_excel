#Esse código é livre e vivo, se vc tem alguma contribuição será bem-vinda. Criado por Bruno Duarte, caso utilize, credite o autor ;) 
from selenium import webdriver as opcoes_selenium_aula #utiliza o Framework selenium e importa as opções do webdriver, para controle do navegador 
from selenium.webdriver.common.keys import Keys #importa as chaves para utilizar o selenium com o webdriver
import pyautogui as tempoPausaComputador #importa o modulo pyautogui com o alias 
from selenium.webdriver.common.by import By #importa o "By", para buscar os campos no código HTML do site 



meuNavegador = opcoes_selenium_aula.Chrome() #realiza a abertura do navegador Google Chrome
meuNavegador.get('https://www.google.com.br/') #Utiliza o metodo get para acessar o site do Google 
tempoPausaComputador.sleep(4) #Aguarda tempo de 4 segundos para processamento 
meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")#Seleciona o campo de pesquisa do Google, a letra "q" representa o elemento do campo de pesquisa, localizado na opção de Inspecionar do navegador 
tempoPausaComputador.sleep(4) #Aguarda tempo de 4 segundos para processamento
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN) #Retorna para o campo name q 
tempoPausaComputador.sleep(4) #Aguarda tempo de 4 segundos para processamento
 
