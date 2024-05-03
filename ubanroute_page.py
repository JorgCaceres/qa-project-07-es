# SE CREO LA PAGINA URBAN ROUTE PARA LA CLASE DEL MISMO NOMBRE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import retrive_phonecode


class UrbanRoutesPage:
    #SE REMPLAZARON LAS RUTAS XPHAT SOLICITADAS
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_button = (By.CLASS_NAME, 'button.round')
    comfort_card = (By.XPATH, '//img[@alt="Comfort"]')
    comfort_card_information = (By.XPATH, '//button[@data-for="tariff-card-4"]')
    add_number_button = (By.XPATH, '//div[@class="np-button"]')
    add_number_text = (By.XPATH, '//div[@class="np-text"]')
    input_number = (By.XPATH, '//div[@class="np-input"]/div')
    write_number = (By.ID, 'phone')
    full_number_button = (By.CLASS_NAME, "button.full")
    code_phone_field = (By.ID, 'code')
    confirmation_code_button = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    add_payment_method = (By.CSS_SELECTOR, '.pp-button.filled >.pp-text')
    add_credit_card = (By.CSS_SELECTOR, '.section.active>.pp-selector>.pp-row.disabled')
    input_card_number = (By.CLASS_NAME, 'card-input')
    input_code_number = (By.XPATH, '//div[@class="card-code-input"]/input')
    submit_card_button = (By.XPATH, '//div[@class="pp-buttons"]/button[@type="submit"]')
    close_payment_button =(By.CSS_SELECTOR, '.payment-picker.open>.modal>.section.active>button')
    payment_text = (By.CLASS_NAME, 'pp-value-text')
    payment_icon = (By.XPATH, '//div[@class="pp-value-container"]/img')
    input_comment = (By.ID, 'comment')
    comment_field = (By.CSS_SELECTOR, '.tariff-picker.shown>.form>:nth-child(3)>div')
    error_message_comment = (By.XPATH, '//div[contains(text(), "Longitud máxima 24")]')
    blanket_switch_button = (By.CLASS_NAME, 'r-sw')
    blanket_switch_state = (By.CSS_SELECTOR, '.r-sw > div > input')
    counter_icecream = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-value')
    add_icecream_button = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-plus')
    smart_button_call = (By.CLASS_NAME, 'smart-button-wrapper')
    order_section = (By.XPATH, '//div[@class="order-body"]')
    card_license_plate = (By.XPATH, '//div[@class="order-number"]')

    def __init__(self, driver):
        self.driver = driver

    # Bloque seleccionar ruta
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

# Bloque seleccionar tarifa comfort
    def wait_for_call_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.call_button))
    def click_call_button(self):
        self.driver.find_element(*self.call_button).click()
    def select_comfort(self):
        self.driver.find_element(*self.comfort_card).click()
    def check_comfort_active(self):
        return self.driver.find_element(*self.comfort_card_information).is_displayed()
    def set_comfort_tariff(self):
        self.wait_for_call_button()
        self.click_call_button()
        self.select_comfort()
        self.check_comfort_active()

# Bloque rellenar el numero de telefono
    def click_add_number(self):
        self.driver.find_element(*self.add_number_button).click()
    def click_input_number_field(self):
        self.driver.find_element(*self.input_number).click()
    def set_number_input(self, number):
        self.driver.find_element(*self.write_number).send_keys(number)
    def click_full_number_button(self):
        self.driver.find_element(*self.full_number_button).click()
    def set_code_phone(self):
        self.driver.find_element(*self.code_phone_field).send_keys(retrive_phonecode.retrieve_phone_code(self.driver))
    def click_confirmation_code_button(self):
        self.driver.find_element(*self.confirmation_code_button).click()
    def get_add_number_text(self):
        return self.driver.find_element(*self.add_number_text).text
    def set_phone_number(self, number):
        self.click_add_number()
        self.click_input_number_field()
        self.set_number_input(number)
        self.click_full_number_button()
        self.set_code_phone()
        self.click_confirmation_code_button()


#Bloque agregar tarjeta
    def click_add_paymenth(self):
        self.driver.find_element(*self.add_payment_method).click()
    def click_add_card(self):
        self.driver.find_element(*self.add_credit_card).click()
    def set_card_number(self, card_number):
        self.driver.find_element(*self.input_card_number).send_keys(card_number)
    def set_code_number(self, code_number):
        self.driver.find_element(*self.input_code_number).send_keys(code_number)
    def click_submit_card(self):
        self.driver.find_element(*self.input_card_number).click()
        self.driver.find_element(*self.submit_card_button).click()
    def close_payment(self):
        self.driver.find_element(*self.close_payment_button).click()
    def set_credit_card(self, card_number, code_number):
        self.click_add_paymenth()
        self.click_add_card()
        self.set_card_number(card_number)
        self.set_code_number(code_number)
        self.click_submit_card()
        self.close_payment()

    def get_pp_text(self):
        return self.driver.find_element(*self.payment_text).text
    def get_pp_icon(self):
        return self.driver.find_element(*self.payment_icon).get_attribute("alt")

# Bloque agregar comentario para el conductor
    def click_comment_field(self):
        self.driver.find_element(*self.comment_field).click()
    def write_comment(self, message):
        self.driver.find_element(*self.input_comment).send_keys(message)
    def set_comment_driver(self, message):
        self.click_comment_field()
        self.write_comment(message)
    def get_error_message_comment(self):
        return self.driver.find_element(*self.error_message_comment).text
    def get_input_comment(self):
        return self.driver.find_element(*self.input_comment).get_property('value')

# Bloque pedir manta y panuelos
    def click_blanket_switch(self):
        self.driver.find_element(*self.blanket_switch_button).click()
    def get_blanket_switch_state(self):
        return self.driver.find_element(*self.blanket_switch_state).is_selected()

# Bloque pedir helados
    def click_add_icecream(self):
        self.driver.find_element(*self.add_icecream_button).click()
        self.driver.find_element(*self.add_icecream_button).click()
    def get_icecream_count(self):
        return self.driver.find_element(*self.counter_icecream).text

# Bloque pedir el taxi
    def click_smart_button(self):
        self.driver.find_element(*self.smart_button_call).click()
    def get_order_section_status(self):
        return self.driver.find_element(*self.order_section).is_displayed()

# Informacion del conductor
    def get_driver_information(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.card_license_plate))
        return self.driver.find_element(*self.card_license_plate).is_displayed()
