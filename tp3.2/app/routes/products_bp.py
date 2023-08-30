from flask import Blueprint
from ..controllers.productsController import productController

product_bp=Blueprint('product_bp',__name__)
product_bp.route('/products', methods = ['POST'])(productController.create_product)
product_bp.route('/products/<int:product_id>' ,methods = ['GET'])(productController.get_product)
product_bp.route('/products' ,methods = ['GET'])(productController.get_products)