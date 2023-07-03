from collections import defaultdict
from typing import DefaultDict

import pytest

from configuration.ui import UIConfig
from models.webdriver.driver.page import Page
from page_objects.header_object import Header


@pytest.fixture(scope="function")
def try_header(page: Page, ui_config: UIConfig) -> Header:
    new_page = Header(page=page)
    new_page.visit(ui_config.base_url)
    yield new_page
    new_page.delete_all_cookies()

@pytest.fixture(scope="function")
def categories_schema() -> DefaultDict[str, str]:
    cat_paths = {
        "clothes": "3-clothes",
        "accessories": "6-accessories",
        "art": "9-art"
    }
    d = defaultdict(lambda: "Not expected URL")
    d.update(cat_paths)
    return d
# @pytest.fixture(scope="function")
# def get_cat(try_header: Header):
#     cat_len = try_header.get_categories().length()
#     for cat in range(cat_len)



