from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from models.types.webdriver.driver.element import ElementInterface
    from models.types.webdriver.driver.element_wait import ElementWaitInterface
    from models.types.webdriver.driver.page import PageInterface


class ElementShouldInterface(ABC):
    _page: "PageInterface"
    _wait: "ElementWaitInterface"
    _element: "ElementInterface"

    @abstractmethod
    def __init__(
            self,
            page: "PageInterface",
            element: "ElementInterface",
            timeout: int,
            ignored_exceptions: list = None
    ):
        ...

    @abstractmethod
    def be_clickable(self) -> "ElementInterface":
        ...

    @abstractmethod
    def be_hidden(self) -> "ElementInterface":
        ...

    @abstractmethod
    def be_visible(self) -> "ElementInterface":
        ...

    @abstractmethod
    def have_text(self, text: str, case_sensitive=True) -> "ElementInterface":
        ...
