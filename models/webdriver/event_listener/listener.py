import datetime
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from configuration.structions import root_dir
from utils.logger_loguru.logger import logger


class CustomListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        ...

    def after_navigate_to(self, url, driver):
        ...

    def before_navigate_back(self, driver):
        ...

    def after_navigate_back(self, driver):
        ...

    def before_navigate_forward(self, driver):
        ...

    def after_navigate_forward(self, driver):
        ...

    def before_find(self, by, value, driver):
        ...

    def after_find(self, by, value, driver):
        ...

    def before_click(self, element, driver):
        ...

    def after_click(self, element, driver):
        ...

    def before_change_value_of(self, element, driver):
        ...

    def after_change_value_of(self, element, driver):
        ...

    def before_execute_script(self, script, driver):
        ...

    def after_execute_script(self, script, driver):
        ...

    def before_close(self, driver):
        ...

    def after_close(self, driver):
        ...

    def before_quit(self, driver):
        ...

    def after_quit(self, driver):
        ...

    def on_exception(self, exception, driver: WebDriver):
        shoots_path = root_dir.joinpath('utils', 'screenshots')
        shoot_time = datetime.datetime.now().timestamp()

        title = driver.title
        version = driver.caps['browserVersion'].replace('.', '_')

        shoots_path = shoots_path.joinpath(
            driver.name,
            f'v_{version}__page_{title}__exception_{shoot_time}.png'
        )
        driver.save_screenshot(shoots_path)

        allure.attach.file(shoots_path)

        logger.error(exception)
