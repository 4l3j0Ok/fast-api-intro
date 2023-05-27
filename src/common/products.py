from common import constants
from models.products import Product
from pydantic import ValidationError

#TODO Docker for db

def validate_product(product, keys=[]):
    try:
        Product.validate(Product(**product)) if isinstance(product, dict) else Product.validate(product)
        return True, None
    except ValidationError as vex:
        fault_keys = [error["loc"][0] for error in vex.errors() if str(error["loc"][0]) in keys] if keys \
            else [error["loc"][0] for error in vex.errors()]
        if fault_keys:
            return False, constants.ERR_SCHEMA.format(err_args=", ".join(fault_keys))
        return True, None


def get_products(id: int = None):
    if id:
        product = next((product for product in constants.PRODUCTS if product.id == id), None)
        if not product:
            return False, constants.ERR_PRODUCT_NOT_FOUND
        return True, product
    return constants.PRODUCTS


def save_product(product):
    success, result = validate_product(product)
    if not success:
        return False, result
    if get_products(product.id)[0]:
        return False, constants.ERR_PRODUCT_ALREADY_EXISTS.format(id=product.id)
    constants.PRODUCTS.append(product)
    return True, constants.MSG_SUCCESS_SAVE


def update_product(product):
    success, result = validate_product(product, keys=["id"])
    if not success:
        return False, str(result)
    success, current_product = get_products(product["id"])
    if not success:
        return False, constants.ERR_PRODUCT_NOT_FOUND
    index = constants.PRODUCTS.index(current_product)
    updated_product = current_product.dict()
    updated_product.update(product)
    new_product = Product(**updated_product)
    if new_product == current_product:
        return False, constants.ERR_PRODUCT_NOT_CHANGED.format()
    constants.PRODUCTS[index] = new_product
    return True, constants.PRODUCTS[index]


def remove_product(product_id):
    success, current_product = get_products(product_id)
    if not success:
        return False, constants.ERR_PRODUCT_NOT_FOUND
    index = constants.PRODUCTS.index(current_product)
    constants.PRODUCTS.pop(index)
    return True, "Producto eliminado con éxito"
