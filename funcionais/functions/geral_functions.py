# -*-coding: UTF-8 -*-


def page_adm_home(driver):
    link_home = driver.find_element_by_xpath("//a[text()='Onecloud']")
    link_home.click()