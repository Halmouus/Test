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
connection.close()
