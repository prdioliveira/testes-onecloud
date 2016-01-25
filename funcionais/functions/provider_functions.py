# -*-coding: UTF-8 -*-

import os
from selenium.common.exceptions import NoSuchElementException

diretorio = os.path.dirname(os.path.realpath(__file__))
completo = diretorio + '/arquivo/lista.txt'
def cadastrar_provider(driver):
    driver.maximize_window()
    arq = open(completo, 'r')
    linha = arq.readlines()
    link_provider = driver.find_element_by_link_text("Providers")
    link_provider.click()
    in_success = 'The provider "'
    end_success = '" was added successfully.'

    for x in range(len(linha)):
        try:
            driver.implicitly_wait(2)
            link_add_provider = driver.find_element_by_class_name("addlink")
            link_add_provider.click()
            cp_nome_prvder = driver.find_element_by_id("id_name")
            cp_nome_prvder.send_keys(linha[x])
            btn_saved = driver.find_element_by_name("_save")
            btn_saved.click()
            assert in_success + linha[x] + end_success == driver.find_element_by_xpath("//li[@class='success']").text
        except NoSuchElementException:
            pass