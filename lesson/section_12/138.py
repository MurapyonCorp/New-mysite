import mysql.connector

conn = mysql.connector.connect(host = '54.250.198.253')

cursor = conn.cursor()

cursor.execute('CREATE DATABASE test_mysql_database')

cursor.close()
conn.close()