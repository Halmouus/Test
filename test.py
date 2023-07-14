import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='debian-sys-maint',
    password='49hxI0eaEvaazj9B',
    auth_plugin='mysql_native_password',
        
)
cursor = connection.cursor()

connection.close()
