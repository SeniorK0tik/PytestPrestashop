from locators.cart_locators import RightBlock
from locators.registration_locators import RegistrationForm


class OrderLocators:
    """http://localhost/order?controller=order"""
    guest_nav_link = {"css": ".nav-link[aria-controls='checkout-guest-form']"}
    signin_nav_link = {"css": ".nav-link[aria-controls='checkout-login-form']"}

    step_title_blocks = {"css": ".step-title"}

    tab_content = {"css": " .tab-content"}


class PersonalInfo(RegistrationForm):
    """http://localhost/order?controller=order"""
    personal_checkout_info_step = {"css": "#checkout-personal-information-step"}
    p_info_step = personal_checkout_info_step["css"]

    # PostComplete
    account_link = {"css": p_info_step + " .identity a"}

class Address:
    """http://localhost/order?controller=order"""
    address_checkout_step = {"css": "#checkout-addresses-step"}
    addr_step = address_checkout_step["css"]
    # PreComplete
    alias = {"css": addr_step + " #field-alias"}
    company = {"css": addr_step + " #field-company"}
    address_1 = {"css": addr_step + " #field-address1"}
    address_2 = {"css": addr_step + " #field-address2"}
    city = {"css": addr_step + " #field-city"}
    state_select = {"css": addr_step + " #field-id_state"}
    postcode = {"css": addr_step + " #field-postcode"}
    country_select = {"css": addr_step + " #field-id_country"}
    phone = {"css": addr_step + " #field-phone"}
    same_addr_checkbox = {"css": addr_step + " #use_same_address"}

    # PostComplete
    delivery_address_boxes = {"css": addr_step + ".js-address-item"}
    edit_addr_link = {"css": " .edit-addres"}



class Delivery:
    delivery_checkout_step = {"css": "#checkout-delivery-step"}

class Payment:
    payment_checkout_step = {"css": "#checkout-payment-step"}

class CollapsedDetails:
    collapsed_details = {"css": RightBlock.right_block["css"] + " .cart-summary-product-list"}
    media_list = {"css": collapsed_details["css"] + " .media-list"}
    cart_item_blocks = {"css": media_list["css"] + " .media"}

    media_left = {"css": " .media-left"}
    media_body = {"css": " .media-body"}
    product_name = {"css": media_body["css"] + " .product-name"}
    product_qty = {"css": media_body["css"] + " .product-quantity"}
    product_price = {"css": media_body["css"] + " .product-line-info"}

