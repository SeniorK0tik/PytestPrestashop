import random
from typing import Union

from selenium.webdriver.remote.webdriver import WebElement

from models.types.webdriver.driver.element import ElementInterface
from models.types.webdriver.driver.elements import ElementsInterface
from models.types.webdriver.driver.page import PageInterface
from models.webdriver.driver.element import Element
from models.webdriver.driver.elements_should import ElementsShould


class Elements(ElementsInterface):

    def __init__(
        self,
        page: PageInterface,
        web_elements: list[WebElement],
        locator: Union[tuple[str, str], None]
    ):

        self._list: list[ElementInterface] = [
            Element(page, element, None) for element in web_elements
        ]
        self._page = page
        self.locator = locator

    def length(self) -> int:
        """
        This function returns the length of a list stored in a class attribute.
        :return: the length of the list stored in the private attribute `_list`. The length is returned as an integer.
        """
        return len(self._list)

    def is_empty(self) -> bool:
        """
        The function checks if a list has zero elements and returns a boolean value.
        :return: a boolean value (True or False) indicating whether the list is empty or not. If the length of the list
         is zero, then the function returns True, indicating that the list is empty. Otherwise, it returns False,
         indicating that the list is not empty.
        """
        return self.length() == 0

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> ElementsShould:
        """
        This function returns an instance of the ElementsShould class with a specified wait time and list of ignored
        exceptions.

        :param timeout: The timeout parameter is an integer value that specifies the maximum amount of time (in seconds)
        that the code should wait for an element to appear or become interactable before timing out and raising an
        exception. If a timeout value is not provided, the default timeout value from the driver's configuration will be
        used, defaults to 0
        :type timeout: int (optional)
        :param ignored_exceptions: `ignored_exceptions` is a list of exceptions that should be ignored during the
         waiting period. If any of the exceptions in the list are raised during the waiting period, they will not
         cause the wait to fail. This can be useful in cases where certain exceptions are expected and should not cause
         the test to
        :type ignored_exceptions: list
        :return: The method is returning an instance of the `ElementsShould` class, which takes four arguments:
        `self._page`, `self`, `wait_time`, and `ignored_exceptions`. The `wait_time` argument is determined by the
         `timeout` parameter passed to the method or by the default `wait_time` value of the driver.
          The `ignored_exceptions` parameter is an optional list of exceptions that
        """
        if timeout:
            wait_time = timeout
        else:
            wait_time = self._page.config.driver.wait_time
        return ElementsShould(self._page, self, wait_time, ignored_exceptions)

    def get_list(self) -> list[ElementInterface]:
        """
        This function returns a list of ElementInterface instances.
        :return: The method `get_list` is returning a list of `ElementInterface` instances, which is specified
         in the return type annotation `-> list[ElementInterface]`.
        """
        return self._list

    def get_random_element(self) -> Element:
        """
        This Python function returns a random element from a list.
        :return: a randomly selected element from the list stored in the object. The return type is an instance of the
        `Element` class.
        """
        random_el = random.choice(self._list)
        return random_el
