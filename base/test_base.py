# -*- coding: utf-8 -*-
'''
Created on Aug 19, 2019

@author: flba
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from resources.data import PAGE_URL
from resources.variables import BROWSER


class TestBase():

    @pytest.fixture(scope="function", autouse=True)
    def _setup_teardown_test(self):
        if BROWSER == "chrome":
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif BROWSER == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(PAGE_URL)
        yield
        self.driver.quit()

    def get_element_by_id(self, name):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, name)))

    def get_element_by_name(self, name):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, name)))

    def get_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def get_text_of_element(self, element):
        return element.text

    def click_element(self, element):
        element.click()

    def edit_element(self, element, value):
        element.send_keys(value)