# -*-coding: UTF-8 -*-


def acessar_site(driver, url):
    driver.get(url)
    logo = driver.find_element_by_xpath("//a[text()='OneCloud']").text
    assert "OneCloud" == logo
