from locators.common_locators import MiscLocators, VerticalKB


class CartLocators(VerticalKB):
    ...
    # cart_grid = {"css": ".cart-grid"}
class LeftBlock(CartLocators):
    left_block = {"css": ".cart-grid-body"}
    continue_shopping_link = {"css": left_block["css"] + " .a.label:has(.material-icons)"}

    cart_items_block = {"css": left_block["css"] + " .cart-items"}
    cart_item = {"css": cart_items_block["css"] + " .cart-item"}

    grid_left = {"css": cart_item["css"] + "div[class*='grid-left'"}
    product_image = {"css": cart_item["css"] + " .product-image"}

    grid_body = {"css": cart_item["css"] + "div[class*='grid-body']"}
    product_name = {"css": grid_body["css"] + " a.label"}
    product_price_block = {"css": grid_body["css"] + " .product-price"}
    regular_price = {"css": product_price_block["css"] +  MiscLocators.regular_price["css"]}
    discount_percentage = {"css": product_price_block["css"]  + MiscLocators.product_percentage["css"]}
    current_price_block = {"css": product_price_block["css"] + " .current-price"}
    product_size_block = {"css": grid_body["css"] + " .size"}
    product_color_block = {"css": grid_body["css"] + " .color"}

    grid_right = {"css": cart_item["css"] + " div[class*='grid-right']"}
    input_number_area = {"css": grid_right["css"] + " input[class*='product-quantity']"}
    vertical_btn_area = {"css": grid_right["css"] + VerticalKB.vertical_btn_area["css"]}
    product_price = {"css": grid_right["css"] + " .product-price"}
    trash_btn = {"css": grid_right["css"] + " .remove-from-cart"}

class RightBlock(CartLocators):
    right_block = {"css":  ".cart-grid-right"}
    cart_summary = {"css": right_block["css"] + " .cart-summary"}
    summary_lines = {"css": cart_summary["css"] + " .cart-summary-line"}

    checkout_btn = {"css": cart_summary["css"] + " .btn-primary"}




