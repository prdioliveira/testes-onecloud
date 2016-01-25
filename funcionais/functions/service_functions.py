# -*-coding: UTF-8 -*


import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException

diretorio = os.path.dirname(os.path.realpath(__file__))


def cadastrar_service_provider_aws(driver):
    completo = diretorio + '/arquivo/provider_aws.txt'
    arq = open(completo, 'r')
    linha = arq.readlines()
    link_services = driver.find_element_by_link_text("Services")
    link_services.click()
    in_success = 'The service "'
    end_success = '" was added successfully.'

    x = 0
    while x < len(linha):
        try:
            driver.implicitly_wait(2)
            link_add_service = driver.find_element_by_class_name("addlink")
            link_add_service.click()
            cp_nome_service = driver.find_element_by_id("id_name")
            cp_nome_service.send_keys(linha[x].replace('\n', ''))
            select = driver.find_element_by_id("id_provider")
            select.send_keys("Amazon Web Services")
            x += 1
            cpu = driver.find_element_by_id("id_cpu")
            cpu.send_keys(linha[x].replace('\n', ''))
            x += 1
            mem = driver.find_element_by_id("id_memory")
            mem.send_keys(linha[x].replace('\n', ''))
            x += 1
            disk = driver.find_element_by_id("id_disk")
            disk.send_keys(linha[x].replace('\n', ''))
            x += 1
            price = driver.find_element_by_id("id_price")
            price.send_keys(linha[x].replace('\n', ''))
            x += 1
            btn_saved = driver.find_element_by_name("_save")
            btn_saved.click()
            assert in_success + linha[x - 5].replace('\n', '') + end_success == \
                   driver.find_element_by_xpath("//li[@class='success']").text
        except NoSuchElementException:
            pass


def cadastrar_service_provider_hp(driver):
    completo = diretorio + '/arquivo/provider_hp.txt'
    arq = open(completo, 'r')
    linha = arq.readlines()
    in_success = 'The service "'
    end_success = '" was added successfully.'

    x = 0
    while x < len(linha):
        try:
            driver.implicitly_wait(2)
            link_add_service = driver.find_element_by_class_name("addlink")
            link_add_service.click()
            cp_nome_service = driver.find_element_by_id("id_name")
            cp_nome_service.send_keys(linha[x].replace('\n', ''))
            select = driver.find_element_by_id("id_provider")
            select.send_keys("HP Public Cloud")
            x += 1
            cpu = driver.find_element_by_id("id_cpu")
            cpu.send_keys(linha[x].replace('\n', ''))
            x += 1
            mem = driver.find_element_by_id("id_memory")
            mem.send_keys(linha[x].replace('\n', ''))
            x += 1
            disk = driver.find_element_by_id("id_disk")
            disk.send_keys(linha[x].replace('\n', ''))
            x += 1
            price = driver.find_element_by_id("id_price")
            price.send_keys(linha[x].replace('\n', ''))
            x += 1
            btn_saved = driver.find_element_by_name("_save")
            btn_saved.click()
            assert in_success + linha[x - 5].replace('\n', '') + end_success == \
                   driver.find_element_by_xpath("//li[@class='success']").text
        except NoSuchElementException:
            pass


def cadastrar_service_provider_microsoft(driver):
    completo = diretorio + '/arquivo/provider_hp.txt'
    arq = open(completo, 'r')
    linha = arq.readlines()
    in_success = 'The service "'
    end_success = '" was added successfully.'

    x = 0
    while x < len(linha):
        try:
            driver.implicitly_wait(2)
            link_add_service = driver.find_element_by_class_name("addlink")
            link_add_service.click()
            cp_nome_service = driver.find_element_by_id("id_name")
            cp_nome_service.send_keys(linha[x].replace('\n', ''))
            select = driver.find_element_by_id("id_provider")
            select.send_keys("Microsoft Azure")
            x += 1
            cpu = driver.find_element_by_id("id_cpu")
            cpu.send_keys(linha[x].replace('\n', ''))
            x += 1
            mem = driver.find_element_by_id("id_memory")
            mem.send_keys(linha[x].replace('\n', ''))
            x += 1
            disk = driver.find_element_by_id("id_disk")
            disk.send_keys(linha[x].replace('\n', ''))
            x += 1
            price = driver.find_element_by_id("id_price")
            price.send_keys(linha[x].replace('\n', ''))
            x += 1
            btn_saved = driver.find_element_by_name("_save")
            btn_saved.click()
            assert in_success + linha[x - 5].replace('\n', '') + end_success == \
                   driver.find_element_by_xpath("//li[@class='success']").text
        except NoSuchElementException:
            pass


def update_service(driver):
    msg_success = 'The service "m1.medium" was changed successfully.'
    try:
        link_services = driver.find_element_by_link_text("Services")
        link_services.click()
        link_nm_service = driver.find_element_by_xpath("//a[text()='m1.medium']")
        link_nm_service.click()
        select = driver.find_element_by_id("id_provider")
        select.send_keys("Microsoft Azure")
        btn_saved = driver.find_element_by_name("_save")
        btn_saved.click()
        assert msg_success == driver.find_element_by_xpath("//li[@class='success']").text
    except NoSuchElementException:
        pass