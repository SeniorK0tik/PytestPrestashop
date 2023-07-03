from abc import ABC, abstractmethod
from typing import Union

from selenium.webdriver.remote.webdriver import WebElement

from models.types.webdriver.driver.element import ElementInterface
from models.types.webdriver.driver.page import PageInterface


class ElementsInterface(ABC):
    _list: list[ElementInterface]
    _page: PageInterface
    locator: Union[tuple[str, str], None]

    @abstractmethod
    def __init__(
            self,
            page: PageInterface,
            web_elements: list[WebElement],
            locator: Union[tuple[str, str], None]
    ):
        ...

    @abstractmethod
    def length(self) -> int:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...
