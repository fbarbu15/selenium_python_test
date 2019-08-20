# -*- coding: utf-8 -*-
"""
Created on Aug 19, 2019

@author: flba
"""

from steps.steps_hotels_page import StepsHotelsPage


class TestHotelsPage(StepsHotelsPage):

    def test_01_hotels_page_loaded_correctly(self):
        self.given_focus_on_hotels_page()
        self.then_hotels_page_has_correct_title()
        self.and_hotels_page_has_correct_url()

    def test_02_search_for_hotels_in_brasov(self):
        self.given_focus_on_hotels_page()
        self.and_set_destination_brasov()
        self.and_select_second_suggestion()
        self.and_checkin_is_on_date(26)
        self.and_checkout_is_on_date(28)
        self.when_seach_is_clicked()
