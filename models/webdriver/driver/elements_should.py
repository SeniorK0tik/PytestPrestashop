from selenium.common.exceptions import TimeoutException

from models.types.webdriver.driver.elements import ElementsInterface
from models.types.webdriver.driver.elements_should import ElementsShouldInterface
from models.types.webdriver.driver.page import PageInterface

from utils.logger_loguru.logger import logger


class ElementsShould(ElementsShouldInterface):
    """ElementsShould API: Commands (aka Expectations) for the current list of Elements"""

    def __init__(
            self,
            page: PageInterface,
            elements: "ElementsInterface",
            timeout: int,
            ignored_exceptions: list = None
    ):
        self._page = page
        self._elements = elements
        self._wait = page.wait(
            timeout=timeout,
            use_self=True,
            ignored_exceptions=ignored_exceptions
        )

    def have_length(self, length: int) -> bool:
        """
        An expectation that the number of elements in the list is equal to the given length
        """
        logger.info("Elements.should().have_length(): %s", length)

        try:
            if self._elements.length() == length:
                return True

            locator = self._elements.locator
            value = self._wait.until(
                lambda drvr: len(drvr.find_elements(*locator)) == length
            )
        except TimeoutException:
            value = False

        if value:
            return True

        raise AssertionError(f"Length of elements was not equal to {length}")

    def not_be_empty(self) -> ElementsInterface:
        """An expectation that the list has at least one element"""
        from models.webdriver.driver.elements import Elements

        logger.info("Elements.should().not_be_empty()")

        try:
            if not self._elements.is_empty():
                return self._elements

            locator = self._elements.locator
            value = self._wait.until(lambda drvr: drvr.find_elements(*locator))
        except TimeoutException:
            value = False

        if isinstance(value, list):
            return Elements(self._page, value, self._elements.locator)

        raise AssertionError("List of elements was empty")
