# -*-coding: UTF-8 -*-

import unittest
from selenium import webdriver
from funcionais.functions.login_functions import login_sucess
from funcionais.functions.login_functions import login_valida_campos
from funcionais.functions.service_functions import cadastrar_service_provider_aws
from funcionais.functions.service_functions import update_service
from funcionais.functions.service_functions import cadastrar_service_provider_hp
from funcionais.functions.service_functions import cadastrar_service_provider_microsoft
from funcionais.functions.provider_functions import cadastrar_provider
from funcionais.functions.provider_functions import update_provider
from funcionais.functions.provider_functions import delete_one_provider
from funcionais.functions.provider_functions import delete_all_provider
from funcionais.functions.site_functions import acessar_site


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_1login(self):
        print 'Testes de login...'
        login_valida_campos(self.driver, "http://localhost:8000/admin")
        login_sucess(self.driver, "http://localhost:8000/admin")

    def test_2cadastrar_provider(self):
        print 'Testes de cadastro de provedor...'
        login_sucess(self.driver, "http://localhost:8000/admin")
        cadastrar_provider(self.driver)

    def test_3cadastrar_service(self):
        print 'Testes de cadastro de serviços...'
        login_sucess(self.driver, "http://localhost:8000/admin")
        cadastrar_service_provider_aws(self.driver)
        cadastrar_service_provider_hp(self.driver)
        cadastrar_service_provider_microsoft(self.driver)

    def test_4update_service_provider(self):
        login_sucess(self.driver, "http://localhost:8000/admin")
        update_service(self.driver)
        update_provider(self.driver)

    def test_5acesso_site(self):
        print 'Testes de acesso ao site...'
        acessar_site(self.driver, "http://localhost:8000")

    def test_6delete_service_provider(self):
        login_sucess(self.driver, "http://localhost:8000/admin")
        delete_one_provider(self.driver)
        delete_all_provider(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()