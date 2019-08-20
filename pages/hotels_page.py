# -*- coding: utf-8 -*-
'''
Created on Aug 19, 2019

@author: flba
'''

from base.test_base import TestBase


class HotelsPage(TestBase):

    TAB_ID = "skhot"
    TAB_TITLE_XPATH = "//h1[@class='BpkText_bpk-text__WdiWu BpkText_bpk-text--lg__2psIk HomePage_HomePage__heading__298c7']"
    DESTINATION_NAME = "destination-autosuggest"
    DESTINATION_SUGGESTION = "react-autowhatever-1--item-{0}"
    CHECKIN_ID = "checkin"
    CHECKOUT_ID = "checkout"
    CALEDAR_DATE = "//td[@class='BpkCalendarGrid_bpk-calendar-grid__date__XwUff']//button[@class='BpkCalendarDate_bpk-calendar-date__3zKNP']//span[contains(text(),'{0}')]"
    SEARCH_BUTTON_ID = "search-button"
    SEARCH_BUTTON_XPATH = "//button[@class='BpkButton_bpk-button__2Jd0U BpkButton_bpk-button--large__1Qijo SearchControls_SearchControls__cta__3nH4P']"

    def click_hotels_tab(self):
        self.click_element(self.get_element_by_id(self.TAB_ID))

    def get_title_text(self):
        return self.get_text_of_element(self.get_element_by_xpath(self.TAB_TITLE_XPATH))

    def insert_destination(self, value):
        self.edit_element(self.get_element_by_name(self.DESTINATION_NAME), value)

    def confirm_second_suggestion(self):
        self.click_element(self.get_element_by_id(self.DESTINATION_SUGGESTION.format("1"))) # 1 is for second suggestion

    def click_checkin(self):
        self.click_element(self.get_element_by_id(self.CHECKIN_ID))

    def click_checkout(self):
        self.click_element(self.get_element_by_id(self.CHECKOUT_ID))

    def select_calendar_date(self, value):
        self.click_element(self.get_element_by_xpath(self.CALEDAR_DATE.format(value)))

    def click_search(self):
        self.click_element(self.get_element_by_xpath(self.SEARCH_BUTTON_XPATH))