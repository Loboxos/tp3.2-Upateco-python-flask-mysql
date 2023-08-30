from ..models.products import products
from flask import request,jsonify

class productController:
    @classmethod
    def create_product(self):
        data = request.json
        product = products.create_product(
            product_name=data.get('product_name'),
            brand_id=data.get('brand_id'),
            category_id=data.get('category_id'),
            model_year=data.get('model_year'),
            list_price=data.get('list_price')
        )
        if product:
            return jsonify({}), 201
        else:
            return jsonify({"error": "Error al registrar el producto"}), 500
