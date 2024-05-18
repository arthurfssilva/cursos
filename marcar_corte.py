import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule

# Função para marcar o horário no site do barbeiro
def marcar_horario():
    # Inicializa o WebDriver (certifique-se de que o ChromeDriver está no seu PATH)
    driver = webdriver.Chrome()

    try:
        # Navegue até o site do barbeiro
        driver.get("https://cashbarber.com.br/brlopesbarbershop/login")
        
        
        # Aguarde o carregamento do site
        time.sleep(5)

        #email para logar
        email = driver.find_element(By.NAME, "email")
        email.send_keys("freitas.arthut@gmail.com")

        #senha para logar
        password = driver.find_element(By.NAME, "password")
        password.send_keys("@Rth1598")

        time.sleep(5)
        
        password.send_keys(Keys.RETURN)
            
            
        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        novo_agendamento = driver.find_element(By.CSS_SELECTOR, ".btn")  # Ajuste conforme necessário
        novo_agendamento.click()

        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        filial = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_selecione___XrzC")  # Ajuste conforme necessário
        filial.click()

        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        filial1 = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_containerFilial__2o_i8")  # Ajuste conforme necessário
        filial1.click()
        
        # Aguarde o carregamento da página de agendamento 
        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        barbeiro = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_barbeiroIcon__2S1vL")  # Ajuste conforme necessário
        barbeiro.click()
        
        # Aguarde o carregamento da página de agendamento 
        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        servico = driver.find_element(By.LINK_TEXT, "Corte")  # Ajuste conforme necessário
        servico.click()

        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        confirmar = driver.find_element(By.CSS_SELECTOR, ".btn Novo-agendamento_buttonBottomSheet__2DO4t")  # Ajuste conforme necessário
        confirmar.click()
                
        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        dia = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_containerSelected__2L9DP")  # Ajuste conforme necessário
        dia.click()  

        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        horario = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_horariosContainer__16Wfd")  # Ajuste conforme necessário
        horario.click()
        
        time.sleep(30)
        
        
        # Preencha os campos necessários
        campo_data = driver.find_element(By.ID, "campo_data")
        campo_data.send_keys("2024-05-24")  # Exemplo de data
        
        campo_hora = driver.find_element(By.ID, "campo_hora")
        campo_hora.send_keys("17:30")
        
        botao_confirmar = driver.find_element(By.ID, "botao_confirmar")
        botao_confirmar.click()

        # Aguarde a confirmação
        time.sleep(5)

    finally:
        # Feche o navegador
        driver.quit()

# Agende a execução da função para toda quinta-feira às 23:41
schedule.every().friday.at("23:41").do(marcar_horario)

# Mantém o script em execução e lida com interrupções
# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script interrompido pelo usuário")
# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")
# finally:
#     print("Limpando recursos e encerrando o script.")

marcar_horario()