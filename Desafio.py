from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Define que a janela do chrome será maximizada.
chrome_options = Options()
chrome_options.add_argument("start-maximized")

# Criado o driver (webdriver), instanciado nas opções definidas anteriormente.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessada a URl da página inicial do youtube.
driver.get('https://www.youtube.com')
time.sleep(3)

# Busca na tela pelo elemento que representa a caixa de pesquisa, digita o nome do canal e, faz o envio com RETURN.
pesquisa = driver.find_element(By.NAME, 'search_query')
pesquisa.send_keys('Qontrol Alt | Software para Gestão de TI')
pesquisa.send_keys(Keys.RETURN)
time.sleep(3)

# Busca o primeiro canal encontrado dentre os resultados e acessa ele.
primeiro_canal = driver.find_element(By.XPATH, '(//a[@id="main-link"])[1]')
primeiro_canal.click()
time.sleep(3)

# Acessa a aba de vídeos do canal.
aba_videos = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]/div[1]')
aba_videos.click()
time.sleep(3)

# Abre o último vídeo postado.
ultimo_postado = driver.find_element(By.XPATH, '(//ytd-thumbnail[@class="style-scope ytd-rich-grid-media"])[1]')
ultimo_postado.click()
time.sleep(3)

# Armazena a quantidade de views, e realiza sua formatação para texto.
quantidade_views = driver.find_element(By.XPATH, '//*[@id="info"]/span[1]')
views_texto = quantidade_views.text

# Expande a descrição do vídeo.
expandir_descricao = driver.find_element(By.XPATH, '//*[@id="expand"]')
expandir_descricao.click()
time.sleep(3)

# Armazena a descrição do vídeo, e realiza sua formatação para texto.
descricao = driver.find_element(By.XPATH, '//*[@id="description-inline-expander"]/yt-attributed-string')
descricao_text = descricao.text

# Busca dentro da descrição formatada todos os elementos que contenham '#'.
hashtags = re.findall(r'#\w+', descricao_text)
time.sleep(5)

# Clica no botão "Mostrar Transcrição", na descrição do vídeo.
abrir_transcricao = driver.find_element(By.XPATH, '//*[@id="primary-button"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
abrir_transcricao.click()
time.sleep(3)

# Armazena a transcrição do vídeo, e realiza sua formatação para texto.
transcricao = driver.find_element(By.XPATH, '//*[@id="segments-container"]')
transcricao_text = transcricao.text

# Faz a limpeza dos períodos e concatena o texto, podendo retorná-lo por extenso.
transcricao_sem_horarios = re.sub(r'\d{1,2}:\d{2}', '', transcricao_text)
texto_concatenado = ' '.join(transcricao_sem_horarios.split())

# Imprime para o usuário, todas as informações solicitadas (visualizações, tags e transcrição do vídeo).
print(views_texto)
print(hashtags)
print(texto_concatenado)

# Encerra o driver.
driver.quit()
