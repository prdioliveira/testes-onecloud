# -*-coding: UTF-8 -*-


def login_valida_campos(driver, url):
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(2)

    # bind
    field_username = driver.find_element_by_id("id_username")
    field_password = driver.find_element_by_id("id_password")
    btn_login = driver.find_element_by_xpath("//input[@value='Log in']")

    # set
    field_username.send_keys("")
    field_password.send_keys("")
    btn_login.click()
    assert "This field is required." in driver.find_element_by_css_selector("form").text

    # bind
    field_username = driver.find_element_by_id("id_username")
    field_password = driver.find_element_by_id("id_password")
    btn_login = driver.find_element_by_xpath("//input[@value='Log in']")

    # set
    field_username.send_keys("admin")
    field_password.send_keys("")
    btn_login.click()
    assert "This field is required." in driver.find_element_by_css_selector("form").text

    # bind
    field_username = driver.find_element_by_id("id_username")
    field_password = driver.find_element_by_id("id_password")
    btn_login = driver.find_element_by_xpath("//input[@value='Log in']")

    # set
    field_username.clear()
    field_password.send_keys("admin")
    btn_login.click()
    assert "This field is required." in driver.find_element_by_css_selector("form").text


def login_sucess(driver, url):
    # User
    user = "admin"
    pwd = "admin"

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(2)

    field_username = driver.find_element_by_id("id_username")
    field_password = driver.find_element_by_id("id_password")
    btn_login = driver.find_element_by_xpath("//input[@value='Log in']")

    # Auth
    field_username.send_keys(user)
    field_password.send_keys(pwd)
    btn_login.click()

    # Asserts
    # Validation
    user_logged = driver.find_element_by_xpath("//div[@id='user-tools']/strong").text
    assert "ADMIN" == user_logged
    assert "Site administration | Django site admin" == driver.title