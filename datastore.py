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

    def fetchProductCategories(self):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT id, name, is_night_use, is_day_use FROM ProductCategories WHERE is_day_use = true")
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

