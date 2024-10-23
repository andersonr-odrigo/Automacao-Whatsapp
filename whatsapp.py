from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
import urllib.parse

planilha = pd.read_excel('Base_Whatsapp.xlsx')

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)
navegador.get("https://web.whatsapp.com/")

sleep(15)

for i, (mensagem, numero) in enumerate(zip(planilha["MENSAGEM"], planilha["CELULAR"])):

    mensagem_formatada = urllib.parse.quote(mensagem)

    if pd.notna(mensagem) and pd.notna(numero):

        link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_formatada}"
        navegador.get(link)
        sleep(10)

        # Verificação de número inválido
        try:
            btn_numero_invalido = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button")
            btn_numero_invalido.click()
            print(f"O número {numero} é inválido")
        except:
            navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
            sleep(1)
            print(f"Mensagem enviada com sucesso para o número {numero}\n")
        
    else:

        pessoa = planilha["NOME"].loc[i]
        print(f"Erro ao enviar mensagem para {pessoa} número: {numero}\n")
        with open('erros.txt', 'a') as log_file:
            log_file.write(f"Erro ao enviar mensagem para {pessoa} número: {numero}\n")

print("Script finalizado")