from ..models.products import products
from flask import request,jsonify

class productController:
    @classmethod
    def create_product(self):
        data = request.json
        product = products(
            product_id=None, 
            product_name=data.get('product_name'),
            brand=data.get('brand_id'),
            category=data.get('category_id'),
            model_year=data.get('model_year'),
            list_price=data.get('list_price')
        )
        products.create_product(product)
        return jsonify({}), 201
      
    
    @classmethod
    def get_product(self,product_id):
        product = products.get_product_by_id(product_id) 
        if product:
            response = {
                "brand": {
                    "brand_id": product.brand["brand_id"],
                    "brand_name": product.brand["brand_name"]
                },
                "category": {
                    "category_id": product.category["category_id"],
                    "category_name": product.category["category_name"]
                },
                "list_price": str(product.list_price),
                "model_year": product.model_year,
                "product_id": product.product_id,
                "product_name": product.product_name
            }
            
            return jsonify(response), 200
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    
    @classmethod
    def get_products(self):
        products_list = products.get_all_products()
        response = []
        for product in products_list:
            #print(product)
            product_data = {
            "brand": {
                "brand_id": product["brand"]["brand_id"],
                "brand_name": product["brand"]["brand_name"]
            },
            "category": {
                "category_id": product["category"]["category_id"],
                "category_name": product["category"]["category_name"]
            },
            "list_price": str(product["list_price"]),
            "model_year": product["model_year"],
            "product_id": product["product_id"],
            "product_name": product["product_name"]
        }
            response.append(product_data)

        return jsonify(response), 200
   
   
    @classmethod
    def modificar_producto(cls, product_id):
        data = request.json

        product = products.get_product_by_id(product_id)

        if not product:
            return jsonify({"error": "Producto no encontrado"}), 404

        if 'product_name' in data:
            product.product_name = data['product_name']
        if 'brand_id' in data:
            product.brand['brand_id'] = data['brand_id']
        if 'category_id' in data:
            product.category['category_id'] = data['category_id']
        if 'model_year' in data:
            product.model_year = data['model_year']
        if 'list_price' in data:
            product.list_price = data['list_price']

        if product.guardar_cambios_en_db(product):  
            return jsonify({}), 200
        else:
            return jsonify({"error": "Error al guardar los cambios"}), 500

