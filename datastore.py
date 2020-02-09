import mysql.connector
from models.productcategory import ProductCategory

class DataStore:
    connection = None

    #def __init__(self):

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="skincare",
            passwd="ujrlufiejrblckidihdjclfejnfnuiti",
            database="skincare"
        )

    def fetchProductCategories(self, is_day):
        mycursor = self.connection.cursor()
        query = "SELECT id, name, is_night_use, is_day_use FROM ProductCategories WHERE "
        if is_day:
            query += "is_day_use = true"
        else:
            query += "is_night_use = true"
            
        mycursor.execute(query)
        products = []
        for product_raw in mycursor.fetchall():
            product = ProductCategory(
                product_raw[0], 
                product_raw[1], 
                product_raw[2], 
                product_raw[3]
            )
            products.append(product)
        return products


