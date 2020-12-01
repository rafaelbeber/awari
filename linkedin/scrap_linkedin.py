# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:09:54 2020

@author: Rafael Beber
"""

# Imports
from selenium import webdriver
from time import sleep


# Parametros
CHROME_PATH = r'C:\Users\rafae\Google Drive\Awari\Codigo\Whatsapp\chromedriver.exe'
LINKEDIN_URL = 'https://www.linkedin.com/jobs/search?keywords=Ci%C3%AAncia%20de%20dados&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'


# Execução
if __name__ == '__main__':
    # Criar uma instancia do Google Crhome pelo Selenium
    driver = webdriver.Chrome(CHROME_PATH)
    driver.implicitly_wait(10)
     
    # Acessar URL do Linkedin
    driver.get(LINKEDIN_URL)
   
    # Pegar Lista de Resultdos
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricoes = []
    
    # Loop em cima de todos os resultados
    while True:
        # For loop para coletar as descrições das vagas
        for r in resultados[len(lista_descricoes):]:
            # Clicar na descrição
            r.click()
            # Aguardar 2 segundos
            sleep(2)
            try:
                # pega o elemento com a descrição
                descricao = driver.find_element_by_class_name('description')
                # Anexa o texto na lista
                lista_descricoes.append(descricao.text)
            except:
                print('Error')
                pass
        
        resultados = driver.find_elements_by_class_name('result-card')
        
        # Saida do while loop
        if len(lista_descricoes) == len(resultados):
            break
    
    # Imprime lista no console
    print(lista_descricoes)
    
    # Adiciona descrição na varialvel com todas as descrições
    descricao_salvar ='\n'.join(lista_descricoes)
    
    # Salva em arquivo as descrições
    with open('descricoes_vagas.txt', 'w', encoding="utf-8") as f:
        f.write(descricao_salvar)
    
    # Fecha o Google Chrome
    driver.quit()

