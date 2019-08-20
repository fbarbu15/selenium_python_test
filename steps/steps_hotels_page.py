# -*- coding: utf-8 -*-
'''
Created on Aug 19, 2019

@author: flba
'''

from pages.hotels_page import HotelsPage
from time import sleep


class StepsHotelsPage(HotelsPage):

    def given_focus_on_hotels_page(self):
        self.click_hotels_tab()

    def then_hotels_page_has_correct_title(self):
        assert self.get_title_text() == "Hoteluri, apartamente şi hosteluri"

    def and_hotels_page_has_correct_url(self):
        assert self.driver.current_url == "https://www.skyscanner.ro/hoteluri", "Page url not correct"
