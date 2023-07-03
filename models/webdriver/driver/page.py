from time import sleep
from typing import Union, Optional

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.exceptions import MaxRetryError

from selenium.webdriver.support import expected_conditions as EC
from configuration.ui import UIConfig
from models.types.webdriver.driver.page import PageInterface
from models.webdriver.driver.element import Element
from models.webdriver.driver.elements import Elements
from models.webdriver.driver.page_wait import PageWait
from models.webdriver.factory.factory import build_from_config
from utils.logger_loguru.logger import logger


class Page(PageInterface):
    """
    Page interface that representing interactions with page 
    like finding locators, opening url etc.
    """

    def __init__(self, config: UIConfig, listener: Optional[AbstractEventListener] = None):
        self.config = config
        self.listener = listener
        self._webdriver = None
        self._wait = None

    def init_webdriver(self) -> WebDriver:
        """Initialize WebDriver using the UIConfig"""
        self._webdriver = build_from_config(self.config)

        self._wait = PageWait(
            self, self._webdriver, self.config.driver.wait_time, ignored_exceptions=None
        )

        if self.config.driver.page_load_wait_time:
            self.set_page_load_timeout(self.config.driver.page_load_wait_time)

        if self.config.viewport.maximize:
            self.maximize_window()
        else:
            self.viewport(
                self.config.viewport.width,
                self.config.viewport.height,
                self.config.viewport.orientation
            )
        self._webdriver = EventFiringWebDriver(self._webdriver, self.listener) if self.listener else self._webdriver
        return self._webdriver

    @property
    def webdriver(self) -> WebDriver:
        """The current instance of Selenium's `WebDriver` API."""
        return self.init_webdriver() if self._webdriver is None else self._webdriver

    @property
    def url(self) -> str:
        """Get the current page's URL"""
        return self.webdriver.current_url

    def visit(self, url: str) -> "Page":
        """Navigate to the given URL"""
        normalized_url = url if url.startswith(
            'http') else (self.config.base_url + url)

        logger.info("Page.visit() - Visit URL: `%s`", normalized_url)

        self.webdriver.get(normalized_url)
        return self

    def reload(self) -> "Page":
        """Reload (aka refresh) the current window"""
        logger.info("Page.reload() - Reloading the page")

        self.webdriver.refresh()
        return self

    def wait_until_stable(self) -> WebDriver:
        """Waits until webdriver will be stable"""
        logger.info("Page.wait_until_stable() - Page wait until driver stable")

        try:
            return self.webdriver
        except MaxRetryError:
            sleep(0.5)
            self.wait_until_stable()

    def get_css(self, css: str, timeout: int = None) -> Element:
        """Finds the DOM element that match the CSS selector."""
        logger.info(
            "Page.get_css() - Get the element with css: {}", format(css)
        )

        by = By.CSS_SELECTOR

        if timeout == 0:
            element = self.webdriver.find_element(by, css)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, css),
                f"Could not find an element with css: `{css}`"
            )
        return Element(self, element, locator=(by, css))

    def get_xpath(self, xpath: str, timeout: int = None) -> Element:
        """
        Finds the DOM element that match the XPATH selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.
        """
        logger.info(
            "Page.get_xpath() - Get the element with xpath: `%s`", xpath
        )

        by = By.XPATH

        if timeout == 0:
            element = self.webdriver.find_element(by, xpath)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, xpath),
                f"Could not find an element with xpath: `{xpath}`"
            )

        return Element(self, element, locator=(by, xpath))

    def find_css(self, css: str, timeout: int = None) -> Elements:
        """
        Finds the DOM elements that match the CSS selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.
        """
        by = By.CSS_SELECTOR
        elements: list[WebElement] = []

        logger.info(
            "Page.find_css() - Get the elements with css: `%s`", css
        )

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, css)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, css),
                    f"Could not find an element with xpath: `{css}`"
                )
        except TimeoutException:
            pass

        return Elements(self, elements, locator=(by, css))

    def find_xpath(self, xpath: str, timeout: int = None) -> Elements:
        """
        Finds the DOM elements that match the XPATH selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.
        """
        by = By.XPATH
        elements: list[WebElement] = []

        logger.info(
            "Page.find_xpath() - Get the elements with xpath: `%s`", xpath
        )

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, xpath)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, xpath),
                    f"Could not find an element with xpath: `{xpath}`"
                )
        except TimeoutException:
            pass

        return Elements(self, elements, locator=(by, xpath))

    def wait(
            self, timeout: int = None, use_self: bool = False, ignored_exceptions: list = None
    ) -> Union[WebDriverWait, PageWait]:
        """The Wait object with the given timeout in seconds"""
        if timeout:
            return self._wait.build(timeout, use_self, ignored_exceptions)

        return self._wait.build(self.config.driver.wait_time, use_self, ignored_exceptions)

    def quit(self):
        """Quits the driver"""
        logger.info(
            "Page.quit() - Quit page and close all windows from the browser session"
        )

        self.webdriver.quit()

    def screenshot(self, filename: str) -> str:
        """Take a screenshot of the current Window"""
        logger.info("Page.screenshot() - Save screenshot to: `%s`", filename)

        self.webdriver.save_screenshot(filename)
        return filename

    def maximize_window(self) -> "Page":
        """Maximizes the current Window"""
        logger.info("Page.maximize_window() - Maximize browser window")

        self.webdriver.maximize_window()
        return self

    def execute_script(self, script: str, *args) -> "Page":
        """Executes javascript in the current window or frame"""
        logger.info(
            "Page.execute_script() - Execute javascript `%s` into the Browser", script
        )

        self.webdriver.execute_script(script, *args)
        return self

    def set_page_load_timeout(self, timeout: int) -> "Page":
        """Set the amount of time to wait for a page load to complete before throwing an error"""
        logger.info(
            "Page.set_page_load_timeout() - Set page load timeout: `%s`", timeout
        )

        self.webdriver.set_page_load_timeout(timeout)
        return self

    def viewport(self, width: int, height: int, orientation: str = "portrait") -> "Page":
        """Control the size and orientation of the current context's browser window"""
        logger.info(
            "Page.viewport() - Set viewport width: `%s`, height: `%s`, orientation: `%s`",
            width, height, orientation
        )

        if orientation == "portrait":
            self.webdriver.set_window_size(width, height)
        elif orientation == "landscape":
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError("Orientation must be `portrait` or `landscape`.")
        return self

    def delete_all_cookies(self) -> None:
        logger.info(
            "Page.delete_all_cookies() - Clear browser cookies"
        )

        self.webdriver.delete_all_cookies()

    def check_exact_url(self, expected_url: str) -> None:
        logger.info(
            "Page.check_exact_url() - Check url to be {}".format(expected_url)
        )
        try:
            self.wait(use_self=True).until(EC.url_to_be(expected_url))
        except TimeoutException:
            raise AssertionError('URL is not {}, current is {}', format(expected_url, self.url))

    def check_match_url(self, regex_url: str) -> None:
        logger.info(
            "Page.check_match_url() - Check url should be matched with regex: {}".format(regex_url)
        )
        try:
            self.wait(use_self=True).until(EC.url_matches(regex_url))
        except TimeoutException:
            raise AssertionError('URL is not matched with regex: {}, current URL is {}', format(regex_url, self.url))

    def get_previous_page(self) -> "Page":
        logger.info(
            "Page.get_previous_page() - Step back to previous page"
        )
        self.webdriver.back()
        return self
