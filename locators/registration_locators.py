from locators.base import Locator


class RegistrationForm(Locator):
    radio_button_mr = {"css": ".radio-inline[for='field-id_gender-1']"}
    radio_button_mrs = {"css": ".radio-inline[for='field-id_gender-2']"}
    offers_checkbox = {"css": "input[name='optin']"}
    terms_checkbox = {"css": "input[name='psgdpr']"}
    privacy_checkbox = {"css": "input[name='customer_privacy']"}
    save_button = {"css": ".btn[data-link-action='save-customer']"}
    login_link = {"css": ".register-form a[href*='login']"}