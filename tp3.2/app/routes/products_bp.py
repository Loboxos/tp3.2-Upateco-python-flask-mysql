from flask import Blueprint
from ..controllers.productsController import productController

product_bp=Blueprint('product_bp',__name__)
product_bp.route('/products', methods = ['POST'])(productController.create_product)

