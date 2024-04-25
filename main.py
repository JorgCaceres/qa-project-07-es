import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_button = (By.CLASS_NAME, 'button.round')
    comfort_card = (By.XPATH, '//div[@class="workflow-subcontainer"]/div[2]/div[1]/div[5]')
    add_number_button = (By.XPATH, '//div[@class="np-button"]')
    add_number_text = (By.XPATH, '//div[@class="np-text"]')
    input_number = (By.XPATH, '//div[@class="np-input"]/div[1]')
    write_number = (By.ID, 'phone')
    full_number_button = (By.CLASS_NAME, "button.full")
    code_phone_field = (By.ID, 'code')
    confirmation_code_button = (By.XPATH, '//div[@class="modal"]/div[2]/form/div[@class="buttons"]/button[@type="submit"]')
    add_payment_method = (By.XPATH, '//div[@class="workflow-subcontainer"]/div[2]/div[@class="form"]/div[2]')
    add_credit_card = (By.XPATH, '//div[@class="pp-selector"]/div[3]')
    input_card_number = (By.CLASS_NAME, 'card-input')
    input_code_number = (By.XPATH, '//div[@class="card-code-input"]/input')
    submit_card_button = (By.XPATH, '//div[@class="pp-buttons"]/button[@type="submit"]')
    close_payment_button =(By.XPATH, '//div[@class="app"]/div[2]/div[@class="modal"]/div[1]/button')
    payment_text = (By.CLASS_NAME, 'pp-value-text')
    payment_icon = (By.XPATH, '//div[@class="pp-value-container"]/img')
    input_comment = (By.ID, 'comment')
    comment_field = (By.XPATH, '//div[@class="form"]/div[3]/div[1]')
    error_message_comment = (By.XPATH, '//div[@class="form"]/div[3]/div[@class="error"]')
    blanket_switch_button = (By.XPATH, '//div[@class="reqs-body"]/div[1]/div[1]/div[2]')
    blanket_switch_state = (By.XPATH, '//div[@class="reqs-body"]/div[1]/div[1]/div[2]/div[1]/input')
    counter_icecream = (By.XPATH, '//div[@class="r-group-items"]/div[1]/div[1]/div[2]/div[1]/div[@class="counter-value"]')
    add_icecream_button = (By.XPATH, '//div[@class="r-group-items"]/div[1]/div[1]/div[2]/div[1]/div[@class="counter-plus"]')
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
        return self.driver.find_element(*self.comfort_card).get_attribute('class')
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
        self.driver.find_element(*self.code_phone_field).send_keys(retrieve_phone_code(self.driver))
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



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(1)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_confort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_tariff()
        assert routes_page.check_comfort_active() == "tcard active"

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        assert routes_page.get_add_number_text() == phone_number

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        code_number = data.card_code
        routes_page.set_credit_card(card_number, code_number)
        assert routes_page.get_pp_text() == "Tarjeta"
        assert routes_page.get_pp_icon() == "card"

    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        driver_message = data.message_for_driver
        routes_page.set_comment_driver(driver_message)
        assert routes_page.get_error_message_comment() == 'Longitud máxima 24'
        assert routes_page.get_input_comment() == data.message_for_driver
        time.sleep(2)

    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_switch()
        assert routes_page.get_blanket_switch_state() == True

    def test_add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream()
        assert routes_page.get_icecream_count() == '2'

    def test_find_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        assert routes_page.get_order_section_status() == True
        time.sleep(3)

    def test_wait_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_driver_information() == True
        time.sleep(3)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
