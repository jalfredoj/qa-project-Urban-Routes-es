import time
from selenium import webdriver
from data import data
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from helpers.retrive_code import retrieve_phone_code

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service = Service(), options = chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    def test_options(self):
        self.routes_page.click_on_flash_button()
        self.routes_page.click_to_call_a_taxi_button()
        self.routes_page.click_get_comfort_option()
        self.routes_page.click_get_field_phone_number()
        self.routes_page.click_get_phone()
        self.routes_page.click_get_button_phone()
        time.sleep(5)
        code = retrieve_phone_code(self.driver)
        self.routes_page.enter_confirmation_code(code)
        self.routes_page.get_and_click_submit_button()
        self.routes_page.get_and_click_card_field()
        self.routes_page.get_and_click_add_card()
        self.routes_page.input_field_card_number()
        self.routes_page.get_and_click_submit_card()
        self.routes_page.get_and_click_close_button()
        self.routes_page.click_get_message()
        self.routes_page.get_and_click_blanket_and_tissues_slider()
        self.routes_page.click_ice_cream_twice()
        self.routes_page.click_on_submit_ride_a_taxi()
        self.routes_page.wait_modal_taxi()
        self.routes_page.wait_for_driver_info()

        time.sleep(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()