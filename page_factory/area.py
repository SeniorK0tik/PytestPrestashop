from page_factory.component import Component


class Area(Component):
    @property
    def type_of(self) -> str:
        return 'area'


