import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='debian-sys-maint',
        password='49hxI0eaEvaazj9B',
        auth_plugin='mysql_native_password',
        database='tubun'
    )
    cursor = connection.cursor()
    sql = "INSERT INTO PACK (BRAND, QUANT, PRICE) VALUES (%s, %s, %s)"
    val = ("Marlboro", "20", "39")
    cursor.execute(sql, val)
    connection.commit()
    print("Record inserted successfully!")
except mysql.connector.Error as error:
    print(f"Error inserting record: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
