# -*-coding: UTF-8 -*-

import unittest

from selenium import webdriver

from funcionais.functions.login_functions import login_sucess
from funcionais.functions.login_functions import login_valida_campos
from funcionais.functions.provider_functions import cadastrar_provider
from funcionais.functions.service_functions import cadastrar_service_provider_aws
from funcionais.functions.service_functions import cadastrar_service_provider_hp
from funcionais.functions.service_functions import cadastrar_service_provider_microsoft
from funcionais.functions.site_functions import acessar_site


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        login_valida_campos(self.driver, "http://localhost:8000/admin")
        login_sucess(self.driver, "http://localhost:8000/admin")

    def test_cadastrar_provider(self):
        login_sucess(self.driver, "http://localhost:8000/admin")
        cadastrar_provider(self.driver)

    def test_cadastrar_service(self):
        login_sucess(self.driver, "http://localhost:8000/admin")
        cadastrar_service_provider_aws(self.driver)
        cadastrar_service_provider_hp(self.driver)
        cadastrar_service_provider_microsoft(self.driver)

    def test_acesso_site(self):
        acessar_site(self.driver, "http://localhost:8000")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()