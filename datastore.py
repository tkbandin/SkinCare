import mysql.connector
from models.productcategory import ProductCategory
from models.dailyactivitylog import DailyActivityLog

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
        if self.connection == None:
            self.connect()
        mycursor = self.connection.cursor()
        query = """SELECT 
                        id, 
                        name, 
                        is_night_use, 
                        is_day_use 
                    FROM 
                        ProductCategories 
                    WHERE """
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

    def fetchTodayActivityLog(self, person_id):
        if self.connection == None:
            self.connect()
        mycursor = self.connection.cursor()
        query = """SELECT
                        id, 
                        person_id, 
                        date, 
                        water_intake_oz, 
                        did_use_face_mask, 
                        did_exfoliate 
                    FROM DailyActivityLog 
                    WHERE 
                        person_id = {} 
                        and date = date(NOW())""".format(person_id)
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result == None:
            return None
        activityLog = DailyActivityLog(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5]
        )

        return activityLog

    def createActivityLog(self, person_id):
        if self.connection == None:
            self.connect()
        mycursor = self.connection.cursor()
        query = "INSERT into DailyActivityLog (person_id, date) values ({}, NOW())".format(person_id)
        mycursor.execute(query)
        self.connection.commit()


