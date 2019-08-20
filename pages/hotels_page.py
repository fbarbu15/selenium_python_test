# -*- coding: utf-8 -*-
'''
Created on Aug 19, 2019

@author: flba
'''

from base.test_base import TestBase


class HotelsPage(TestBase):

    TAB_ID = "skhot"
    TAB_TITLE_XPATH = "//h1[@class='BpkText_bpk-text__WdiWu BpkText_bpk-text--lg__2psIk HomePage_HomePage__heading__298c7']"

    def click_hotels_tab(self):
        self.click_element(self.get_element_by_id(self.TAB_ID))

    def get_title_text(self):
        return self.get_text_of_element(self.get_element_by_xpath(self.TAB_TITLE_XPATH))
