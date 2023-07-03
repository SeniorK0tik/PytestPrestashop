from typing import Union, Optional

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebElement
from utils.logger_loguru.logger import logger

from models.types.webdriver.driver.element import ElementInterface
from models.types.webdriver.driver.page import PageInterface
from models.webdriver.driver.element_should import ElementShould


class Element(ElementInterface):
    """Element API: Represents a single DOM webelement and includes the commands to work with it."""

    def __init__(
            self,
            page: PageInterface,
            web_element: WebElement,
            locator: Union[tuple[str, str], None]
    ):
        self._page = page
        self._web_element = web_element
        self.locator = locator

    @property
    def web_element(self) -> WebElement:
        return self._web_element

    def text(self):
        logger.info("Element.text - Get element text")
        return self._web_element.text

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> ElementShould:
        """A collection of expectations for this element"""
        if timeout:
            wait_time = timeout
        else:
            wait_time = self._page.config.driver.wait_time

        return ElementShould(self._page, self, wait_time, ignored_exceptions)

    def click(self, force=False) -> "Element":
        """Clicks the element"""
        logger.info("Element.click() - Click this element")

        if force:
            self._page.webdriver.execute_script(
                "arguments[0].click()",
                self.web_element
            )
        else:
            self.web_element.click()

        return self

    def type(self, value) -> "Element":
        """Simulate a user typing keys into the input"""
        logger.info(
            "Element.type() - Type keys: '{}' into this element", format(value)
        )

        ActionChains(self._page.webdriver).move_to_element(self.web_element).send_keys(value).perform()

        return self

    def fill(self, *args) -> "Element":
        """Fill input element with value"""
        logger.info(
            "Element.fill() - Fill value `%s` into this element", (args,)
        )

        self.web_element.send_keys(args)
        return self

    def get_attribute(self, attribute_name: str) -> Union[str, None]:
        logger.info(
            "Element.get_attribute() - Get the type {} of this element ", format(attribute_name)
        )
        return self.web_element.get_attribute(attribute_name)

    def clear(self) -> "Element":
        """Clears the text of the input or textarea element"""
        logger.info("Element.clear() - Clear the input of this element")

        self.web_element.clear()
        return self

    def is_displayed(self) -> bool:
        """Check that this element is displayed"""

        logger.info(
            "Element.is_displayed() - Check if this element is displayed"
        )

        return self.web_element.is_displayed()

    def is_selected(self) -> bool:
        """Check that this element is selected"""

        logger.info(
            "Element.is_selected() - Check if this element is selected"
        )

        return self.web_element.is_selected()

    def move_to(self, ac: ActionChains = None) -> ActionChains:
        """Move to the element"""
        logger.info(
            "ActionChains.move_to() - Move to Element"
        )
        ac = ActionChains(self._page.webdriver) if not ac else ac
        return ac.move_to_element(self.web_element)

    def send_keys(self, key: Keys) -> None:
        logger.info(
            "Element.send_keys() - Send key: {} to element".format(key)
        )
        self.web_element.send_keys(key)
