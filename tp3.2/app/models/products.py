from ..database import DatabaseConnection
class products:
    def __init__(self, product_id,product_name,brand,category,model_year,list_price):
        self.product_id = product_id
        self.product_name = product_name
        self.brand = brand
        self.category = category
        self.model_year = model_year
        self.list_price = list_price

    @classmethod
    def get_product_by_id(cls, producto_id):
        query = '''
        SELECT
            p.product_id,
            p.product_name,
            b.brand_id,
            b.brand_name,
            c.category_id,
            c.category_name,
            p.model_year,
            p.list_price
        FROM
            products p
            JOIN brands b ON p.brand_id = b.brand_id
            JOIN categories c ON p.category_id = c.category_id
        WHERE
            p.product_id = %s
        '''
        params = (producto_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return products(
                product_id=result[0],
                product_name=result[1],
                brand={"brand_id": result[2], "brand_name": result[3]},
                category={"category_id": result[4], "category_name": result[5]},
                model_year=result[6],
                list_price=result[7]
            )
        else:
            return None

    @classmethod
    def create_product(cls, product):
        query = '''
        INSERT INTO products (product_name, brand_id, category_id, model_year, list_price)
        VALUES (%s, %s, %s, %s, %s)
        '''
        values = (product.product_name, product.brand, product.category, product.model_year, product.list_price)

        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True