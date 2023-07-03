import allure
from selenium.common import StaleElementReferenceException

from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def should_be_clickable(self, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is clickable'):
            try:
                element = self.get_element(**kwargs)
                element.should().be_clickable()
            except StaleElementReferenceException:
                self.should_be_clickable(**kwargs)
