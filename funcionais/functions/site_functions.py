# -*-coding: UTF-8 -*-
from selenium.common.exceptions import NoSuchElementException


def acessar_site(driver, url):
    driver.get(url)
    logo = driver.find_element_by_xpath("//a[text()='OneCloud']").text
    assert "OneCloud" == logo

def ordenar_precos(driver):
    try:
        driver.maximize_window()
        driver.implicitly_wait(2)
        cp_preco = driver.find_element_by_xpath("//a[text()='Preço']")
        f_price = driver.find_element_by_xpath("//tr[1]/td[6]").text
        l_price = driver.find_element_by_xpath("//tr[10]/td[6]").text

        first_price = float(f_price)
        last_price = float(l_price)

        if first_price > last_price:
            cp_preco.click()
            assert "Nome" == driver.find_element_by_xpath("//th[text()='Nome']").text

        else:
            assert "Nome" == driver.find_element_by_xpath("//th[text()='Nome']").text
    except NoSuchElementException:
        pass