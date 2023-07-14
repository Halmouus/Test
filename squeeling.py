import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='debian-sys-maint',
    password='49hxI0eaEvaazj9B',
    auth_plugin='mysql_native_password',
    database='tubun'
    
)
cursor = connection.cursor()
#cursor.execute("CREATE DATABASE tubun")
'''
smokerRecord = """CREATE TABLE SMOKER (
                   USERNAME VARCHAR(20) NOT NULL,
                   PASSWORD VARCHAR(50) NOT NULL,
                   AGE INT NOT NULL)"""
packRecord = """CREATE TABLE PACK (
                   BRAND VARCHAR(20) NOT NULL,
                   LABEL VARCHAR(20),
                   QUANT INT NOT NULL,
                   PRICE INT NOT NULL
                   )"""
cursor.execute(smokerRecord)
cursor.execute(packRecord)
'''
#sql = "INSERT INTO PACK (BRAND, QUANT, PRICE) VALUES (%s, %s, %s)"
#val = [("LM Blue", "20", "27"), ("Camel", "20", "38"), ("Winston", "20", "38"),]
#deletion = "DELETE FROM PACK WHERE BRAND = 'MARLBORO'"
#cursor.executemany(sql, val)
selection = "SELECT BRAND FROM PACK WHERE PRICE = '38'"
cursor.execute(selection)
result = cursor.fetchall()
print(result)
#connection.commit()
connection.close()
