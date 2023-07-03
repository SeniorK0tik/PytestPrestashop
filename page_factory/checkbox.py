import allure

from page_factory.button import Button


class Checkbox(Button):
    @property
    def type_of(self) -> str:
        return 'checkbox'

    def is_selected(self, **kwargs) -> bool:
        with allure.step(f'Checking if {self.type_of} "{self.name}" is selected'):
            element = self.get_element(**kwargs)
            return element.is_selected()
