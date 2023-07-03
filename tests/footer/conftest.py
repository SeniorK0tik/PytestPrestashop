from collections import defaultdict
from typing import DefaultDict, NamedTuple

import pytest

from configuration.ui import UIConfig
from models.db.mysql_db import PrestaMySQL
from models.webdriver.driver.page import Page
from page_objects.footer_object import Footer

class EmailData(NamedTuple):
    email: str
    response: str


@pytest.fixture(scope="function")
def try_footer(page: Page, ui_config: UIConfig) -> Page:
    new_page = Footer(page=page)
    new_page.visit(ui_config.base_url)
    yield new_page
    new_page.delete_all_cookies()

@pytest.fixture(scope='function', params=[
    ("You have successfully subscribed to this newsletter.",),
    ("This email address is already registered.",)
])
def email_footer(db_config: PrestaMySQL, request: pytest.FixtureRequest) -> EmailData:
    new_email = "faker@mail.ru"
    def delete_user():
        db_config.delete_email_subscriber(new_email)

    request.node.addfinalizer(delete_user)
    return EmailData(new_email, request.param)


@pytest.fixture(scope='function')
def columns_schema() -> DefaultDict[str, str]:
    schema_1 = {
        "prices drop": "prices-drop",
        "new products": "new-products",
        "best sales": "best-sales"
    }
    schema_2 = {
        "delivery": "content/1-delivery",
        "legal notice": "content/2-legal-notice",
        "terms and conditions of use": "content/3-terms-and-conditions-of-use",
        "about us": "content/4-about-us",
        "secure payment": "content/5-secure-payment",
        "contact us": "contact-us",
        "sitemap": "sitemap",
        "stores": "stores"
    }

    # schema_3 = {
    #     "order tracking": "guest-tracking",
    #     "sign in": "login?back=my-account",
    #     "create account": "registration",
    #     "my alerts": "login?redirect=module&module=ps_emailalerts&action=account"
    #
    # }
    schema_3 = {
        "personal info": "login?back=identity",
        "orders": "login?back=history",
        "credit slips": "login?back=order-slip",
        "addresses": "login?back=addresses",
    }

    d = defaultdict(lambda: "Not expected URL")
    d.update(schema_1)
    d.update(schema_2)
    d.update(schema_3)
    return d

# @pytest.fixture(scope='function')
# def account_column_schema() -> DefaultDict[LINK_NAME, URL]:
#     schema = {
#         "order-tracking": "guest-tracking",
#         "sign in": "my-account",
#         "create account": "registration",
#         "my alerts": "login?redirect=module&module=ps_emailalerts&action=account"


    # }
