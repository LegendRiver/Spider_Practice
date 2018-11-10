from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import appsfly_spider.handler.common_helper as fhelper
import os.path as ospath


class CheckLoginStatus:
    def __init__(self, button_id, attribute_name, check_value):
        self._button_id = button_id
        self._attribute_name = attribute_name
        self.check_value = check_value

    def __call__(self, driver):
        account_button = driver.find_element_by_id(self._button_id)
        button_title = account_button.get_attribute(self._attribute_name)
        return button_title == self.check_value


class AFPageHandler:
    def __init__(self, page_conf_file):
        self.page_conf_info = fhelper.read_json_file(page_conf_file)
        self._login_url = self.page_conf_info['loginURL']
        self._input_username = self.page_conf_info['elementUsername']
        self._input_password = self.page_conf_info['elementPassword']
        self._value_username = self.page_conf_info['usernameValue']
        self._value_password = self.page_conf_info['passwordValue']
        self._button_div_class = self.page_conf_info['buttonDivClassname']
        self._button_tag_name = self.page_conf_info['buttonTagName']
        self._act_name_id = self.page_conf_info['accountNameId']
        self._act_name_attribute = self.page_conf_info['accountNameAttribute']

    def get_login_cookies(self, phantomjs_path=''):
        if phantomjs_path:
            driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=ospath.devnull)
        else:
            driver = webdriver.PhantomJS(service_log_path=ospath.devnull)

        try:
            driver.get(self._login_url)

            user_name_input = driver.find_element_by_name(self._input_username)
            password_input = driver.find_element_by_name(self._input_password)
            user_name_input.send_keys(self._value_username)
            password_input.send_keys(self._value_password)

            button_div = driver.find_element_by_class_name(self._button_div_class)
            login_button = button_div.find_element_by_tag_name(self._button_tag_name)
            login_button.submit()

            WebDriverWait(driver, 10).until(CheckLoginStatus(self._act_name_id, self._act_name_attribute,
                                                             self._value_username))
            return driver.get_cookies()

        except Exception:
            print 'login exception'

        finally:
            driver.delete_all_cookies()
            driver.quit()
