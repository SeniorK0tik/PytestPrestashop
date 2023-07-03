from locators.common_locators import MiscLocators, VerticalKB


class QuickViewLocators(VerticalKB):
    quick_view_modal = {"css": "div[id*='quickview-modal']"}
    modal_content = {"css": quick_view_modal["css"] + " .modal-content"}

    product_cover = {"css": modal_content["css"] + " .product-cover"}
    product_images = {"css": modal_content["css"] + " .product-images"}

    product_name = {"css": modal_content["css"] + " .h1"}

    product_prices = {"css": modal_content["css"] + " .product-prices"}
    product_discount_area = {"css": product_prices["css"] + MiscLocators.product_discount["css"]}
    product_regular_price = {"css": product_discount_area["css"] + MiscLocators.regular_price["css"]}

    current_price_area = {"css": product_prices["css"] + " div[class*='has-discount']"}
    current_price = {"css": current_price_area["css"] + " .current-price-value"}

    short_description = {"css": modal_content["css"] + " #product-description-short"}

    product_actions = {"css": modal_content["css"] + " .product-actions"}
    token_form = {"css": product_actions["css"] + " input[name='token']"}
    id_product = {"css": product_actions["css"] + " input[id_product']"}
    product_variants = {"css": product_actions["css"] + " .product-variants"}

    form_control_options = {
        "css": product_variants["css"] + MiscLocators.form_control["css"] + MiscLocators.option["css"]
    }

    add_to_cart_area = {"css": product_actions["css"] + " .product-add-to-cart"}
    qty_area = {"css": add_to_cart_area["css"] + " .qty"}
    input_box = {"css": qty_area["css"] + " input[type='number']"}

    vertical_btn_area = {"css": qty_area["css"] + VerticalKB.vertical_btn_area["css"]}
    add_to_cart_btn = {"css": add_to_cart_area["css"] + MiscLocators.submit_btn["css"]}

    social_sharing_area = {"css": modal_content["css"] + " .social-sharing"}
    facebook_box = {"css": social_sharing_area["css"] + " li[class*='facebook']"}
    twitter_box = {"css": social_sharing_area["css"] + " li[class*='twitter']"}
    pinterest_box = {"css": social_sharing_area["css"] + " li[class*='pinterest']"}