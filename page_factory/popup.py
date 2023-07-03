from page_factory.component import Component


class Popup(Component):
    @property
    def type_of(self) -> str:
        return 'popup'
