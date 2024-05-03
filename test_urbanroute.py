import data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import ubanroute_page


# SE ELIMINO EL USO DE TIME SELEEP

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
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(1)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_confort(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        routes_page.set_comfort_tariff()
        assert routes_page.check_comfort_active() == True

    def test_set_phone_number(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        assert routes_page.get_add_number_text() == phone_number

    def test_add_card(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        card_number = data.card_number
        code_number = data.card_code
        routes_page.set_credit_card(card_number, code_number)
        assert routes_page.get_pp_text() == "Tarjeta"
        assert routes_page.get_pp_icon() == "card"

    def test_write_message(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        driver_message = data.message_for_driver
        routes_page.set_comment_driver(driver_message)
        assert routes_page.get_error_message_comment() == 'Longitud máxima 24'
        assert routes_page.get_input_comment() == data.message_for_driver
        WebDriverWait(self.driver, 3)

    def test_blanket(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        routes_page.click_blanket_switch()
        assert routes_page.get_blanket_switch_state() == True

    def test_add_icecream(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream()
        assert routes_page.get_icecream_count() == '2'

    def test_find_driver(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        assert routes_page.get_order_section_status() == True
        WebDriverWait(self.driver, 3)

    def test_wait_driver_information(self):
        routes_page = ubanroute_page.UrbanRoutesPage(self.driver)
        assert routes_page.get_driver_information() == True
        WebDriverWait(self.driver, 3)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
