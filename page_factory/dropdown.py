from page_factory.component import Component


class DropDown(Component):
    @property
    def type_of(self) -> str:
        return 'dropdown'

