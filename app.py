import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Função para marcar o horário no site do barbeiro
def marcar_horario():
    # Inicializa o WebDriver (certifique-se de que o ChromeDriver está no seu PATH)
    driver = webdriver.Chrome()

    try:
        # Navegue até o site do barbeiro
        driver.get("https://cashbarber.com.br/brlopesbarbershop/login")
        
        # Aguarde o carregamento do site
        time.sleep(5)

        # email para logar
        email = driver.find_element(By.NAME, "email")
        email.send_keys("freitas.arthut@gmail.com")

        # senha para logar
        password = driver.find_element(By.NAME, "password")
        password.send_keys("@Rth1598")

        time.sleep(1)
        
        password.send_keys(Keys.RETURN)
            
        time.sleep(5)
        
        # Localize e clique no botão para marcar um novo horário
        novo_agendamento = driver.find_element(By.CSS_SELECTOR, ".btn")  # Ajuste conforme necessário
        novo_agendamento.click()

        time.sleep(3)
        
        filial = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_selecione___XrzC")  # Ajuste conforme necessário
        filial.click()

        time.sleep(5)
        
        filial1 = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_containerFilial__2o_i8")  # Ajuste conforme necessário
        filial1.click()
        
        time.sleep(5)
        
        barbeiro = driver.find_element(By.CSS_SELECTOR, ".Novo-agendamento_barbeiroIcon__2S1vL")  # Ajuste conforme necessário
        barbeiro.click()
        
        time.sleep(5)
        
        servico = driver.find_element(By.XPATH, "//*[normalize-space(text()) = 'Corte']")
        servico.click()

        time.sleep(5)

        confirmar = driver.find_element(By.XPATH, "//*[normalize-space(text()) = 'Confirmar']")  # Ajuste conforme necessário
        confirmar.click()
                
        time.sleep(5)
        
        opcoes_dias = driver.find_elements(By.CSS_SELECTOR, ".Novo-agendamento_dayNumber__11n5x")

        if opcoes_dias:
            print(f"Encontradas {len(opcoes_dias)} opções de dias.")
            for idx, opcao in enumerate(opcoes_dias):
                print(f"Opção {idx + 1}: {opcao.text}")

            sexta_feira = opcoes_dias[5]
            sexta_feira.click()
            print("Sexta-feira selecionada.")
        else:
            print("Não foram encontradas opções de dias.")

        time.sleep(5)
        
        horario = driver.find_element(By.XPATH, "//*[normalize-space(text()) = '17:20']")  # Ajuste conforme necessário
        horario.click()
        
        time.sleep(5)
        
        horario = driver.find_element(By.XPATH, "//*[normalize-space(text()) = 'Agendar']")  # Ajuste conforme necessário
        horario.click()

        time.sleep(20)

    finally:
        # Feche o navegador
        driver.quit()

class BarberApp(BoxLayout):
    def __init__(self, **kwargs):
        super(BarberApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Marcando horário...')
        self.add_widget(self.label)

class MyApp(App):
    def build(self):
        root = BarberApp()
        # Chamar a função marcar_horario assim que o aplicativo é iniciado
        marcar_horario()
        root.label.text = 'Horário marcado com sucesso!'
        return root

if __name__ == '__main__':
    MyApp().run()
