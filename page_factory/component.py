from typing import Union

import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from models.webdriver.driver.element import Element
from models.webdriver.driver.elements import Elements
from models.webdriver.driver.page import Page


class Component:
    def __init__(self, page: Page, locator: str, name: str, selector: By = By.CSS_SELECTOR) -> None:
        self._page = page
        self._locator = locator
        self._name = name
        self._selector = selector

    def __add__(self, other: Union[str, 'Component']) -> str:
        if isinstance(other, str):
            return self._locator + ' ' + other
        elif isinstance(other, Component):
            if self._selector == other._selector:
                return self._name + ' ' + other._name
            else:
                raise ValueError("Unsupported operation: Components with different locators cannot be added.")
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Component' and '{}'".format(type(other)))

    @property
    def type_of(self) -> str:
        return 'component'

    @property
    def name(self) -> str:
        return self._name

    def get_element(self, **kwargs) -> Element:
        """Gets element By.CSS"""
        locator = self._locator.format(**kwargs)

        with allure.step(f'Getting {self.type_of} with name "{self.name}" and locator "{locator}"'):
            return self._page.get_css(locator)

    def get_elements(self, **kwargs) -> Elements:
        """Gets elements By.CSS"""
        locator = self._locator.format(**kwargs)

        with allure.step(f'Getting {self.type_of}s with name "{self.name}" and locator "{locator}"'):
            return self._page.find_css(locator)

    def get_attribute(self, attribute_name: str, **kwargs) -> str:
        locator = self._locator.format(**kwargs)

        with allure.step(f'Getting the attribute of {self.type_of}s with name "{self.name}" and locator "{locator}"'):
            element = self.get_element(**kwargs)
            return element.get_attribute(attribute_name)

    def click(self, **kwargs) -> None:
        """
        This function clicks on an element with a given name and type and logs the action using Allure.
        """
        with allure.step(f'Clicking {self.type_of} with name "{self.name}"'):
            element = self.get_element(**kwargs)
            element.click()

    def should_be_visible(self, **kwargs) -> None:
        """
        This function checks if a specified element is visible and retries if it encounters a
        StaleElementReferenceException.
        """
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            try:
                element = self.get_element(**kwargs)
                element.should().be_visible()
            except StaleElementReferenceException:
                self.should_be_visible(**kwargs)

    def should_have_text(self, text: str, **kwargs) -> None:
        """
        This function checks if a specified element has a specified text and retries if the element reference is stale.

        :param text: The expected text that the element should have
        :type text: str
        """
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            try:
                element = self.get_element(**kwargs)
                element.should().have_text(text)
            except StaleElementReferenceException:
                self.should_have_text(text, **kwargs)

    def is_displayed(self, **kwargs) -> bool:
        """
        This function checks if a specified element is visible on the page.
        :return: The method `is_displayed()` of the `element` object is being called and its return value
        is being returned by the `is_displayed()` method of the class. The return value is a boolean value
        indicating whether the element is currently displayed on the page or not.
        """
        with allure.step(f'Checking if {self.type_of} "{self.name}" is visible'):
            element = self.get_element(**kwargs)
            return element.is_displayed()

    def should_have_type(self, attribute_name: str,  attribute_value: str, **kwargs) -> None:
        """
        This function checks if an element has a specific type and retries if the element reference is stale.

        :param attribute_name: The name of the attribute that we want to check the type of
        :type attribute_name: str
        :param attribute_value: The parameter "attribute_value" is a string that represents the expected type of an
        attribute of an element. This method checks if the actual type of the attribute matches the expected type
        :type attribute_value: str
        """
        with allure.step(f'Checking that {self.type_of} "{self.name}" has type "{attribute_value}"'):
            try:
                element = self.get_element(**kwargs)
                element.should().have_type(attribute_name, attribute_value)
            except StaleElementReferenceException:
                self.should_have_type(attribute_name, attribute_value, **kwargs)

    def move_to(self, ac: ActionChains = None, **kwargs) -> ActionChains:
        """Move to the component"""
        with allure.step(f'Move to {self.type_of} with name "{self.name}"'):
            element = self.get_element(**kwargs)
            ac = ActionChains(self._page.webdriver) if ac else ac
            return ac.move_to_element(element)

    def send_key(self, key: Keys, **kwargs) -> None:
        with allure.step(f'Send key {key} to {self.type_of} with name "{self.name}"'):
            element = self.get_element(**kwargs)
            element.send_keys(key)
