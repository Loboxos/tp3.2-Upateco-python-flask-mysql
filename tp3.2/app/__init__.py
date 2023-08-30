from flask import Flask,request,jsonify
from config import Config
from .database import DatabaseConnection
from .routes.products_bp import product_bp

from .models import products

def init_app():
 """Crea y configura la aplicación Flask"""

 app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

 app.config.from_object(Config)
 app.register_blueprint(product_bp)


 @app.route('/')
 def saludar():
    return "Inicio de la App"
 #api sin modelo 
 @app.route('/customers',methods=['POST'])
 def registrar_cliente():
   body_params = request.json
   query = "INSERT INTO sales.customers (first_name, last_name, email, phone, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
   params = (
        body_params['first_name'],
        body_params['last_name'],
        body_params['email'],
        body_params.get('phone', ''),
        body_params.get('street', ''),
        body_params.get('city', ''),
        body_params.get('state', ''),
        body_params.get('zip_code', '')
    )
   DatabaseConnection.execute_query(query, params)
   return jsonify({ }), 201

 @app.route('/products/<int:product_id>', methods=['GET'])
 def get_product(product_id):
    product = models.products.products.get_product_by_id(product_id) 
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
 


 return app