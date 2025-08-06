import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from data.data import phone_number, card_number, card_code, message_for_driver


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    flash_button = (By.XPATH, "//div[@class='mode active' and text()='Flash']")
    to_call_a_taxi_button = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    comfort_option = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    field_phone_number = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    input_phone = (By.ID, 'phone')
    button_phone = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    confirmation_input = (By.ID, 'code')
    submit_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")
    card_field = (By.CLASS_NAME, "pp-text")
    add_card = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    field_card_number = (By.ID, "number")
    submit_card = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
    button_close = (By.CSS_SELECTOR, '.payment-picker .close-button')
    input_message = (By.ID, 'comment')
    blanket_and_tissues_slider = (By.CSS_SELECTOR, "span.slider.round")
    ice_cream_add_button = (By.CSS_SELECTOR, '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    submit_ride_a_taxi = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
    modal_taxi = (By.CSS_SELECTOR, '.order.shown > div.order-body')
    driver_info = (By.CSS_SELECTOR, '.order-subbody > div.order-buttons > div:nth-child(1) > div.order-button > img')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(self.from_field)).send_keys(from_address)

    def assert_set_from(self, from_address):
        self.set_from(from_address)
        actual_value = self.driver.find_element(*self.from_field).get_property("value")
        assert actual_value == from_address

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 6).until(
            expected_conditions.presence_of_element_located(self.to_field)).send_keys(to_address)

    def assert_set_to(self, to_address):
        self.set_from(to_address)
        actual_value = self.driver.find_element(*self.from_field).get_property("value")
        assert actual_value == to_address

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')
    def set_route(self,from_address,to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_flash_button(self):
        return WebDriverWait(self.driver,9).until(expected_conditions.element_to_be_clickable(self.flash_button))
    def click_on_flash_button(self):
        self.get_flash_button().click()
        confirm_get_flash_button =self.get_flash_button()
        assert confirm_get_flash_button.is_enabled()

    def get_to_call_a_taxi_button(self):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(self.to_call_a_taxi_button))
    def click_to_call_a_taxi_button(self):
        self.get_to_call_a_taxi_button().click()
        confirm_to_call_a_taxi = self.get_flash_button()
        assert confirm_to_call_a_taxi.is_enabled()

    def get_comfort_option(self):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(self.comfort_option))

    def click_get_comfort_option(self):
        comfort_button = self.get_comfort_option()
        comfort_button.click()
        assert comfort_button.is_enabled(), "Comfort option is not enabled after click"

    def get_field_phone_number(self):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(self.field_phone_number))

    def click_get_field_phone_number(self):
        phone_field = self.get_field_phone_number()
        phone_field.click()
        assert phone_field.is_displayed() and phone_field.is_enabled(), "Phone field is not interactable"

    def get_phone_input(self):
        return WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.input_phone))

    def click_get_phone(self):
        input_field = self.get_phone_input()
        input_field.clear()
        input_field.send_keys(phone_number)

        actual_value = input_field.get_attribute("value")
        assert actual_value == phone_number, f"Expected '{phone_number}', but got '{actual_value}'"

    def get_button_phone(self):
        return WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.button_phone))

    def click_get_button_phone(self):
        button = self.get_button_phone()
        assert button.is_enabled(), "Button 'Siguiente' is not enabled"
        button.click()

    def enter_confirmation_code(self, code):
        confirmation_field = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.confirmation_input))
        confirmation_field.send_keys(code)

        actual_value = confirmation_field.get_attribute("value")
        assert actual_value == code, f"Expected confirmation code '{code}', but got '{actual_value}'"

    def get_and_click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.submit_button))
        assert submit_button.is_enabled(), "Submit button is not enabled"
        submit_button.click()

    def get_and_click_card_field(self):
        card_field = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.card_field))
        assert card_field.is_enabled(), "Card field is not enabled"
        card_field.click()

    def get_and_click_add_card(self):
        add_card_button = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.add_card))
        assert add_card_button.is_enabled(), "Add Card button is not enabled"
        add_card_button.click()

    def get_and_click_field_card_number(self):
        field_card = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.field_card_number))
        assert field_card.is_enabled(), "Card number field is not enabled"
        return field_card

    def input_field_card_number(self):
        field_card = self.get_and_click_field_card_number()
        field_card.click()
        field_card.clear()
        field_card.send_keys(card_number)
        field_card.send_keys(Keys.TAB)

        time.sleep(3)

        active_element = self.driver.switch_to.active_element
        assert active_element.is_enabled(), "Card code field (active element) is not enabled"
        active_element.send_keys(card_code)
        active_element.send_keys(Keys.TAB)

    def get_and_click_submit_card(self):
        submit_btn = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.submit_card))
        assert submit_btn.is_enabled(), "Submit Card button is not enabled"
        submit_btn.click()

    def get_and_click_close_button(self):
        close_btn = WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(self.button_close))
        assert close_btn.is_enabled(), "Close button is not enabled"
        close_btn.click()

    def click_get_message(self):
        input_field_message = WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(self.input_message))
        assert input_field_message.is_enabled(), "Message input field is not enabled"

        self.driver.execute_script("arguments[0].click();", input_field_message)
        input_field_message.clear()
        input_field_message.send_keys(message_for_driver)

    def get_and_click_blanket_and_tissues_slider(self):
        slider = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.blanket_and_tissues_slider))
        assert slider.is_enabled(), "Blanket and Tissues slider is not enabled"
        slider.click()

    def click_ice_cream_twice(self):
        for _ in range(2):
            ice_cream_button = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.ice_cream_add_button))
            assert ice_cream_button.is_enabled(), "Ice cream add button is not enabled"
            ice_cream_button.click()
            time.sleep(0.3)

    def click_on_submit_ride_a_taxi(self):
        submit_btn = WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self.submit_ride_a_taxi))
        assert submit_btn.is_enabled(), "Submit Ride a Taxi button is not enabled"
        submit_btn.click()

    def wait_modal_taxi(self):
        modal = WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located(self.modal_taxi))
        assert modal.is_displayed(), "Taxi modal is not visible"
        return modal

    def wait_for_driver_info(self):
        driver_info = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(self.driver_info))
        assert driver_info.is_displayed(), "Driver info is not visible"
        return driver_info
