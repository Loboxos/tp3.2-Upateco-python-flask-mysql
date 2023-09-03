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
  
  #Ejercicio1.4
 @app.route('/customers/<int:customer_id>', methods = ['PUT'])
 def update_customer(customer_id):
    data = request.json 
    if "email" in data and "phone" in data:
        query = "UPDATE sales.customers SET email = %s, phone = %s WHERE customer_id = %s"
        params = (data["email"], data["phone"], customer_id)

        result = DatabaseConnection.execute_query(query, params)

        if result:
            return {"msg": "Customer updated"}, 200

    return {"msg": "Invalid data or Customer not found"}, 400
  #Ejercicio1.5
 @app.route('/delete/customers/<int:customer_id>', methods=['DELETE'])
 def delete_customer(customer_id):
        query = "DELETE FROM sales.customers WHERE customer_id = %s;"
        params = (customer_id,)
        print(params)
        result = DatabaseConnection.execute_query(query, params)      
        if result is not None:
            return {"msg": "Customer deleted"}, 204
        else:
            return {"error": "Customer not found"}, 404
 return app