# -*- coding: utf-8 -*-
'''
Created on Aug 19, 2019

@author: flba
'''

from pages.hotels_page import HotelsPage


class StepsHotelsPage(HotelsPage):

    def given_focus_on_hotels_page(self):
        self.click_hotels_tab()

    def and_set_destination_brasov(self):
        self.insert_destination("Brasov")

    def and_select_second_suggestion(self):
        self.confirm_second_suggestion()

    def and_checkin_is_on_date(self, day_of_month):
        self.click_checkin()
        self.select_calendar_date(day_of_month)

    def and_checkout_is_on_date(self, day_of_month):
        self.click_checkout()
        self.select_calendar_date(day_of_month)

    def when_seach_is_clicked(self):
        self.click_search()

    def then_hotels_page_has_correct_title(self):
        assert self.get_title_text() == "Hoteluri, apartamente şi hosteluri", "Hotels page title not correct"

    def and_hotels_page_has_correct_url(self):
        assert self.driver.current_url == "https://www.skyscanner.ro/hoteluri", "Page url not correct"
