# -*-coding: UTF-8 -*-

import os
from selenium.common.exceptions import NoSuchElementException
from funcionais.functions.geral_functions import page_adm_home

diretorio = os.path.dirname(os.path.realpath(__file__))
completo = diretorio + '/arquivo/lista.txt'


def cadastrar_provider(driver):
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
            assert in_success + linha[x].replace('\n', '') + end_success == driver.find_element_by_xpath("//li[@class='success']").text
        except NoSuchElementException:
            pass


def update_provider(driver):
    page_adm_home(driver)
    msg_success = 'The provider "Locaweb" was changed successfully.'
    try:
        link_provider = driver.find_element_by_link_text("Providers")
        link_provider.click()
        link_nm_provider = driver.find_element_by_xpath("//a[text()='Microsoft Azure']")
        link_nm_provider.click()
        cp_nome_prvder = driver.find_element_by_id("id_name")
        cp_nome_prvder.clear()
        driver.implicitly_wait(2)
        cp_nome_prvder.send_keys("Locaweb")
        btn_saved = driver.find_element_by_name("_save")
        btn_saved.click()
        assert msg_success == driver.find_element_by_xpath("//li[@class='success']").text
    except NoSuchElementException:
        pass


def delete_one_provider(driver):
    msg_success = 'The provider "Locaweb" was deleted successfully.'
    try:
        link_provider = driver.find_element_by_link_text("Providers")
        link_provider.click()
        link_nm_provider = driver.find_element_by_xpath("//a[text()='Locaweb']")
        link_nm_provider.click()
        btn_delete_prv = driver.find_element_by_xpath("//a[text()='Delete']")
        btn_delete_prv.click()
        assert "Are you sure?" == driver.find_element_by_xpath("//h1[text()='Are you sure?']").text
        btn_confirm_delete_prv = driver.find_element_by_xpath("//input[@type='submit']")
        btn_confirm_delete_prv.click()
        assert msg_success == driver.find_element_by_xpath("//li[@class='success']").text
    except NoSuchElementException:
        pass


def delete_all_provider(driver):
    page_adm_home(driver)
    msg_success = 'Successfully deleted'
    try:
        link_provider = driver.find_element_by_link_text("Providers")
        link_provider.click()
        driver.implicitly_wait(2)
        select_action = driver.find_element_by_xpath("//select[@name='action']")
        select_action.send_keys("Delete selected providers")
        driver.implicitly_wait(2)
        check_all = driver.find_element_by_id("action-toggle")
        check_all.click()
        driver.implicitly_wait(2)
        btn_go_delete = driver.find_element_by_xpath("//button[text()='Go']")
        btn_go_delete.click()
        assert "Are you sure?" == driver.find_element_by_xpath("//h1[text()='Are you sure?']").text
        btn_confirm_delete_prv = driver.find_element_by_xpath("//input[@type='submit']")
        btn_confirm_delete_prv.click()
        assert msg_success in driver.find_element_by_xpath("//li[@class='success']").text
    except NoSuchElementException:
        pass