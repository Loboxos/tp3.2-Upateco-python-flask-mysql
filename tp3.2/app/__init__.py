from flask import Flask,request,jsonify
from config import Config
from .database import DatabaseConnection
from .routes.products_bp import product_bp

def init_app():
 """Crea y configura la aplicación Flask"""

 app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

 app.config.from_object(Config)
 app.register_blueprint(product_bp)
 
 #saludo de inicio
 @app.route('/')
 def saludar():
    return "Inicio de la App"

 #api sin MVC 
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
 
 return app